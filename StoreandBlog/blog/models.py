from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    text_01 = models.CharField(max_length=256)
    title = models.CharField(max_length=256, unique = True)
    qouted_text_01 = models.Field(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_publish_date = models.DateField()

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.title})

    def get_slug(self):
        return self.title
    
    
    
