from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
