from django.urls import path
from .import views

urlpatterns=[
    path('',views.indexFun,name='index')
]