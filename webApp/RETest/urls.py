from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='RETest-index'),
    path('checker', views.checker, name='RETest-checker')
]