from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser


class Login(LoginView):
    form_class = ShopUserLoginForm
    template_name = 'authapp/login_n_register.html'


class Logout(LogoutView):
    next_page = '/'


def log(request):
    data = dict()
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            data['form_is_valid'] = True
            data['form_html'] = reverse('main')
        else:
            data['form_is_valid'] = False
            data['form_html'] = render_to_string('authapp/login_form.html', {'form': form},
                                                 request=request)
    else:
        data['form_html'] = render_to_string('authapp/login_form.html', {'form': ShopUserLoginForm()},
                                             request=request)
    return JsonResponse(data)


def registration(request):
    data = dict()
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            data['form_is_valid'] = True
            register_form.save()
        else:
            data['form_html'] = render_to_string('authapp/reg_form.html', {'form': register_form},
                                                 request=request)

    else:
        data['form_html'] = render_to_string('authapp/reg_form.html', {'form': ShopUserRegisterForm()},
                                             request=request)
    return JsonResponse(data)


class Edit(UpdateView):
    model = ShopUser
    template_name = 'authapp/edit.html'
    success_url = reverse_lazy('main')
    form_class = ShopUserEditForm

    def get_object(self, queryset=None):
        return ShopUser.objects.get(pk=self.request.user.pk)
