from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('401', error_401, name='401'),
    path('success', success, name='success'),
    path('registration/', registration, name='registration'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout')
]