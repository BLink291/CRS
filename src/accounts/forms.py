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

    user_cache = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_('You entered an invalid username.'))

        if not user.is_active:
            raise ValidationError(_('Please verify your account first.'))

        self.user_cache = user
        return username


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username' : 'You can use letters, numbers ',
            }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

       
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('Already an account associated with this email address.'))

        return email




