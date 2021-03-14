from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogs'

urlpatterns = [
    # the app's urls need functions in the views.py file to handle the pages.
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/', views.post, name='post')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
