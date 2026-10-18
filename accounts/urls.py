from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
   

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),

    path('password_reset/',
        PasswordResetView.as_view(
            template_name = "registration/password_reset.html"
        ),
        name="password_reset"),

    path('password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name = "password_reset_done.html"
        ),
        name="password_reset_done" ),

    path('password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name = "password_reset_confirm.html"
        ),
        name='password_reset_confirm'),
]
