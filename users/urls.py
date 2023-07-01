from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('you', views.UserView.as_view(), name='profile'),
    path('user/<str:username>', views.UserView.as_view(), name='userProfile'),
    path('login/', views.LoginView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('register/', views.newUserView.as_view()),
    path('register', views.newUserView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('logout', auth_views.LogoutView.as_view(next_page='home')),
    path('password-reset/', views.PasswordResetView.as_view(), name='passwordReset'),
    path('password-reset', views.PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('delete-account/', views.DeleteAccountView.as_view(), name='delete_account'),
]
