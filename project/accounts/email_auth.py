from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            valid_email = request.POST['email'] == user.email


        except UserModel.DoesNotExist:
            messages.error(request, "Пользователя не существует")
            return None
        else:
            if user.check_password(password) and valid_email:
                return user
        messages.error(request, 'Пользователь с такой почтой не найден')
        return None