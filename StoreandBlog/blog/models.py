from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    text_01 = models.CharField(max_length=256)
    text_02 = models.CharField(max_length=256)
    text_03 = models.TextField()
    title = models.CharField(max_length=256)
    qouted_text_01 = models.Field(max_length=256)
    qouted_text_02 = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_publish_date = models.DateField()

    
