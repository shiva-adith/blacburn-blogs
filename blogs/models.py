from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=600)
    content = models.TextField()
    date_posted = models.DateField(datetime.now().date(), blank=True)
    image = models.ImageField(upload_to='pics')
