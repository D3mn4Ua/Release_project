from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout')
]