from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from users.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                     "mb-3 leading-tight focus:outline-none text-center focus:bg-white",
            "placeholder": _("Email"),
        })
    )
    phone = PhoneNumberField(
        label=_('Phone number'),
        required=True,
        region='IR',
        widget=PhoneNumberPrefixWidget(
            initial='IR',
            attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-center text-gray-700 border border-red-500 '
                         'rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': _('Phone number')
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "description", "password1", "password2", "profile")
        help_texts = {
            'password1': _("Your password shouldn't be fully numeric and should have at least 8 characters."),
        }
        labels = {
            'username': _("User Name"),
            'first_name': _("First Name"),
            'last_name': _("Last Name"),
            'description': _("Description"),
            'password1': _("Password"),
            'password2': _("Repeat Password"),
        }
        widgets = {
            'username': forms.TextInput(attrs={
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none text-center focus:bg-white px-4",
                "placeholder": _("User Name"),
            }),
            'first_name': forms.TextInput(attrs={
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none text-center focus:bg-white px-4",
                "placeholder": _("First Name"),
            }),
            'last_name': forms.TextInput(attrs={
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none text-center focus:bg-white px-4",
                "placeholder": _("Last Name"),
            }),
            'description': forms.Textarea(attrs={
                'rows': 5, 'cols': 30,
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none text-center focus:bg-white px-4",
                "placeholder": _("Placeholder"),
            }),
            'password1': forms.PasswordInput(attrs={
                'autocomplete': 'current-password',
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-white text-center px-4",
                "placeholder": _("Password"),
            }),
            'password2': forms.PasswordInput(attrs={
                'autocomplete': 'current-password',
                "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3"
                         "mb-3 leading-tight focus:outline-none focus:bg-white text-center px-4",
                "placeholder": _("Repeat Password"),
            }),
            "profile": ClearableFileInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'mb-3 leading-tight focus:outline-none text-center focus:bg-white px-4',
                'placeholder': _('Profile picture')
            })

        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 "
                 "mb-3 leading-tight focus:outline-none focus:bg-white text-center",
        'placeholder': 'Email'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': "appearance-none block w-full "
                 "bg-gray-200 text-gray-700 border "
                 "border-red-500 rounded py-3 px-4 mb-3 "
                 "leading-tight focus:outline-none "
                 "focus:bg-white text-center",
        'placeholder': 'Password'
    }))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'email'
        self.fields['username'].widget = forms.TextInput(attrs={
            "class": "",
            "placeholder": "email"
        })
        self.fields['password'].label = 'PassWord'
        self.fields['password'].widget = forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                    "class": "",
                                                                    "placeholder": "Password"
                                                                    })
