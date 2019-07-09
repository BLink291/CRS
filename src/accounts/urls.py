
from django.urls import path

from .views import IndexPageView, LoginView, LogOutView, RegisterationView, ActivateView

app_name = 'accounts'

urlpatterns = [ 
    path('', IndexPageView.as_view(), name = 'index'),
    path('log-in/', LoginView.as_view(), name = 'log_in'),
    path('log-out/', LogOutView.as_view(), name = 'log_out'),
    path('register/', RegisterationView.as_view(), name = 'register'),
    path('activate/<code>/', ActivateView.as_view(), name='activate'),

]



