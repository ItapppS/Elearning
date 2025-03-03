from django.db import models

class PhnUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    age = models.PositiveIntegerField()
    address = models.TextField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


