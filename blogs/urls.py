from django.urls import path
from . import views

urlpatterns = [
    # the app's urls need functions in the views.py file to handle the pages.
    path('', views.index, name='index')
]
