from django import template

from ..models import File

register = template.Library()


@register.simple_tag
def total_files_checked():
    files_count = File.objects.filter(status='CHK').count()
    return files_count


@register.simple_tag
def total_files_unchecked():
    files_count = File.objects.filter(status__in=['NEW', 'UPD']).count()
    return files_count


@register.simple_tag
def total_logs(file_slug):
    logs_count = File.objects.get(slug=file_slug).log_set.all().count()
    return logs_count
