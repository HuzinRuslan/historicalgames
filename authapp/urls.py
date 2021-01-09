from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.Login.as_view(), name='login'),
    path('log/', authapp.log, name='log'),
    path('logout/', authapp.Logout.as_view(), name='logout'),
    path('registration/', authapp.registration, name='registration'),
    path('edit/', authapp.Edit.as_view(), name='edit'),
]
