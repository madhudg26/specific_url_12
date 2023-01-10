from django.urls import path
from app1.views import *


app_name=('pawan')

urlpatterns=[

    path('pawan/',pawan,name='pawan'),
]