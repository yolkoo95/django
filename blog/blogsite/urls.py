from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<slug:slug>', views.post, name='post')
    # variable slug: whatever value from url
]