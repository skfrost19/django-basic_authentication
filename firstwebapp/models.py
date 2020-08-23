from django.db import models

# Create your models here.


class Signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username



class contactus(models.Model):
    name = models.CharField(max_length=25)
    email_address = models.EmailField()
    phone = models.IntegerField()
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name