from django.urls import path
from app2.views import *

app_name=('slogan')

urlpatterns=[

    path('slogan/',slogan,name='slogan')
]