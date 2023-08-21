from django.core.mail import send_mail
from celery import shared_task
import os
import subprocess

@shared_task
def send_logs(log):
    from .settings import (ACCOUNT_EMAIL_VERIFICATION, EMAIL_BACKEND, EMAIL_HOST,
                           EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS)

    subject = "Отчет по файлу"
    message = (f'Добрый день!\n\nВаш файл был успешно проверен.\n'
               f'Имя файла: {log.file.name}\nФайл: {log.file.file.name[6:]}\nОписание: {log.description}')
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
            log = file.log_set.create(file=file)
            file.status = File.Status.CHECKED
            file.save()
            send_logs(log)
