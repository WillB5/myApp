from django.db import models
from django.urls import reverse
# Create your models here.


class User(models.Model):
    username = models.TextField(max_length=30, null=False, default=None)
    password = models.TextField(max_length=30, null=False, default=None)


class Upload(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField(max_length=300, null=True)

    def get_absolute_url(self):
        return reverse('makepost', )
