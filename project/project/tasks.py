import sys
from io import StringIO
import pylint.lint
from celery import shared_task
from django.core.mail import send_mail
from pylint.reporters.text import TextReporter


@shared_task
def send_logs(log):
    from .settings import (EMAIL_HOST_USER)

    subject = "Отчет по файлу"
    message = (f'Добрый день!\n\nВаш файл был успешно проверен.\n'
               f'Дата проверки: {log.created}\nИмя файла: {log.file.name}\nФайл: {log.file.file.name[6:]}\nОтчет:\n {log.description}')
    send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER,
              recipient_list=[log.file.author.email])
    log.send = True
    log.save()


@shared_task
def check_files():
    from main_app.models import File

    files = File.objects.filter(status__in=['NEW', 'UPD', ])
    if files:
        for file in files:
            stdout = sys.stdout
            sys.stdout = StringIO()

            pylint.lint.Run(['--disable=line-too-long,import-error', 'media/' + file.file.name],
                            reporter=TextReporter(sys.stdout), exit=False)

            test = sys.stdout.getvalue()
            sys.stdout.close()
            sys.stdout = stdout

            log = file.log_set.create(file=file, description=test)
            file.status = File.Status.CHECKED
            file.save()
            send_logs(log)
