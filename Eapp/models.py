from django.db import models

# Create your models here.
class PhnUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hashed password storage
    age = models.PositiveIntegerField()
    mobile_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username