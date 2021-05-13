from django.urls import path, include
from .views import *

urlpatterns = [
    path('lab22/', execprocedure, name='proc')
]
