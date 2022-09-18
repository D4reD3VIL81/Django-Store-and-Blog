from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    count = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=256)
    ziba = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.name})

    def get_slug(self):
        return self.name