from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as authLoginView
from django.contrib.auth.views import PasswordResetView as authPasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView

from MiniCodes import settings
from codeisc.models import *
from . import forms


# Create your views here.

class UserView(TemplateView):
    template_name = "users/user_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user if self.request.user.is_authenticated else None
        username = kwargs.get('username', None)
        if username is None:
            user_profile_object = self.request.user if self.request.user.is_authenticated else None
        else:
            user_profile_object = User.objects.get(username=username)
        context['user_profile_object'] = user_profile_object
        answers_by_user_count = Answer.objects.filter(author__username=user_profile_object.username).count()
        codes_by_user_count = Code.objects.filter(author__username=user_profile_object.username).count()
        questions_by_user_count = Code.objects.filter(author__username=user_profile_object.username).count()
        context['answers_count'] = answers_by_user_count
        context['codes_count'] = codes_by_user_count
        context['questions_count'] = questions_by_user_count
        context['user'] = user
        return context


class LoginView(authLoginView):
    template_name = 'users/login_page.html'
    authentication_form = forms.LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()

        if user and not user.is_active:
            form.add_error('username', 'User is deleted.')
            form.add_error('password', 'User is deleted.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_default_redirect_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


class newUserView(SuccessMessageMixin, CreateView):
    template_name = "users/register_page.html"
    form_class = forms.NewUserForm
    success_url = reverse_lazy('profile')
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class PasswordResetView(authPasswordResetView, SuccessMessageMixin):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('profile')


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_account.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user if self.request.user.is_authenticated else None
        context['user'] = user
        return context
