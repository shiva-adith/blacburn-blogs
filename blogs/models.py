from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Post(models.Model):

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=600)
    content = models.TextField()
    date_posted = models.DateField('date published')
    image = models.ImageField(upload_to='pics')

    def __repr__(self):
        return f"Post(title={self.title}, author={self.author}, date={self.date_posted})"

    def __str__(self):
        return f"{self.title}, written by {self.author}, on {self.date_posted}"

    def written_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
