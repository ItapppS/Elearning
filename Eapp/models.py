from django.db import models

class PhnUser(models.Model):

    first_name = models.CharField(max_length=50,default=True)
    last_name = models.CharField(max_length=50,default=True)
    username = models.CharField(max_length=50, unique=True)
    gmail = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, default=True)
    address = models.TextField(max_length=50,default=True)
    mobile_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


#class PhnContact(models.Model):
