from django.urls import path
from cyberpro.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup/', sign_up, name='signup'),
    path('login/', log_in, name='login'),
]