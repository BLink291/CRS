# users/urls.py
from .views import SignUpView
from django.urls import path

urlpatterns = [
    #path('login/', SignUpView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]