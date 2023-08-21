from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from slug import slug

from .forms import LoadFileForm
from .models import File, Log


# Create your views here.
@login_required
def main_page(request):
    files = File.objects.filter(author_id=request.user.id)
    return render(request, 'main_app/main_page.html', context={'files': files})

@login_required
def load_file(request):
    if request.method == 'POST':
        fileform = LoadFileForm(request.POST, request.FILES)
        if fileform.is_valid():
            file = fileform.save(commit=False)
            file.author = request.user
            file.slug = slug(file.name)
            file.save()
            messages.success(request, f'Пользователь {file.author.username} успешно загрузил файл')
            return redirect('/main/')
    else:
        fileform = LoadFileForm()

    return render(request, 'main_app/load_file.html', context={'fileform': fileform})

@login_required
def update_file(request, file_slug, delete=False):
    file = File.objects.get(slug=file_slug)
    if not delete:
        if request.method == 'POST':
            fileform = LoadFileForm(request.POST, request.FILES, instance=file)
            if fileform.is_valid():
                file = fileform.save(commit=False)
                file.status = File.Status.UPDATED
                file.save()
                messages.success(request, f'Пользователь {file.author.username} успешно обновил файл')
                return redirect('/main/')
        else:
            fileform = LoadFileForm(instance=file)
    else:
        messages.success(request, f'Пользователь {file.author.username} успешно удалил файл - {file.name}')
        file.delete()
        return redirect('/main/')
    return render(request, 'main_app/load_file.html', context={'fileform': fileform})

@login_required
def logs_file(request, file_slug):
    file = File.objects.get(slug=file_slug)
    logs = file.log_set.all()

    return render(request, 'main_app/logs_file.html', context={'file': file, 'logs': logs})

