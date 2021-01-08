from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser


class Login(LoginView):
    form_class = ShopUserLoginForm
    template_name = 'authapp/login.html'


class Logout(LogoutView):
    next_page = '/'


class Registration(CreateView):
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    form_class = ShopUserRegisterForm
    success_message = "Your profile was created successfully"


class Edit(UpdateView):
    model = ShopUser
    template_name = 'authapp/edit.html'
    success_url = reverse_lazy('main')
    form_class = ShopUserEditForm

    def get_object(self, queryset=None):
        return ShopUser.objects.get(pk=self.request.user.pk)
