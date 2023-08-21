from django import forms
from django.core.exceptions import ValidationError

from .models import *


class LoadFileForm(forms.ModelForm):
    name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}), label='Название файла')
    description = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control mb-1"}), label='Описание файла')
    file = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control mb-1"}),
                                label='Файл')

    def clean_file(self):
        data = self.cleaned_data['file']

        # check if the content type is what we expect
        content_type = data.content_type
        print(content_type)
        if content_type == 'text/x-python':
            return data
        else:
            raise ValidationError('Неправильное расширение файла. Файл должен быть формата .py')

    class Meta:
        model = File
        fields = ['name', 'description', 'file']