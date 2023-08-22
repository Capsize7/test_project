from django import template
from django.core.cache import cache

from ..models import File

register = template.Library()


@register.simple_tag
def total_files_checked():
    files_count = cache.get('files_count_checked')
    if not files_count:
        files_count = File.objects.filter(status='CHK').count()
        cache.set('files_count_checked', files_count, 60 * 10)
    return files_count


@register.simple_tag
def total_files_unchecked():
    files_count = cache.get('files_count_unchecked')
    if not files_count:
        files_count = File.objects.filter(status__in=['NEW', 'UPD']).count()
        cache.set('files_count_unchecked', files_count, 60 * 10)
    return files_count


@register.simple_tag
def total_logs(file_slug):
    logs_count = cache.get('logs_count')
    if not logs_count:
        logs_count = File.objects.get(slug=file_slug).log_set.all().count()
        cache.set('logs_count', logs_count, 60 * 10)
    return logs_count
