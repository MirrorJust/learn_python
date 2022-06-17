from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request):
    # дял POST пытаемся аутентифицировать пользователя
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # Поптыка выполнить аутентификацию и авторизацию пользователя
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в ситсему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Првоерьте правильность логина и пароля')
    else: # для остальных случаем просто отображаем саму страницу логина
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'app_users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из под своей учетной записи')


class AnotherLogoutView(LogoutView):
    # template_name = 'app_users/logout.html'
    next_page = '/'
