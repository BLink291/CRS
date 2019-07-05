from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View, FormView, TemplateView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import LoginForm, RegisterForm

from django.utils.decorators import method_decorator
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


from django.conf import settings
from .utils import send_activation_email
from .models import Activate

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'accounts/index.html'


class GuestView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)

class LoginView(GuestView, FormView ):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    def form_valid(self, form):
        login(self.request, form.user_cache )
        return redirect('accounts:index')


class LogOutView(LoginRequiredMixin, LogoutView):
    template_name = settings.LOGIN_REDIRECT_URL

class RegisterationView( GuestView, FormView ):
    template_name = 'accounts/registration.html'
    form_class = RegisterForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        user.username = form.cleaned_data['username']

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        #save changes
        user.save()

        if settings.ENABLE_TWO_STEPS_REGISTRATION:
            secret_key = get_random_string(20)

            act = Activate()
            act.secret_key = secret_key
            act.user = user
            act.save()

            send_activation_email( request, user.email, secret_key )
            messages.success( request, _('Successfully registered. Please verify email address.'))
        else:
            raw_password = form.cleaned_data['password1']

            user = authenticate(username=user.username, password=raw_password)
            login( request, user)

            messages.success(request, _('Successfully Registered!'))

        return redirect('accounts:index')

class ActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activate, secret_key=code)

        # Activate profile
        user = act.user
        user.is_active = True
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, _('Email succesfully verified!'))

        return redirect('accounts:log_in')




