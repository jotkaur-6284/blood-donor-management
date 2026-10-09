from django.db import models

# Create your models here.
class RegisterP(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Donor(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    mail=models.EmailField()
    phone=models.CharField(max_length=15)
    blood_group=models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name