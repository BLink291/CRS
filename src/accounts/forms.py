from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.forms import ValidationError

from django.conf import settings

from django import forms



class LoginForm( forms.Form ):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField( widget=forms.PasswordInput, label=_('Password') )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        return username


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    email = forms.EmailField(label=_('Email'), help_text=_('Please type email to get an account activation mail'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('Already an account associated with this email address.'))

        return email




