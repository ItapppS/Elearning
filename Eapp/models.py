from django.db import models
from django.contrib.auth.hashers import make_password

class PhnUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default=True)  # ✅ Required Password
    age = models.PositiveIntegerField(default=True)
    address = models.TextField(max_length=255, default=True)
    mobile_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


#class PhnContact(models.Model):
