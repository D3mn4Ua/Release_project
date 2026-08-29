from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]