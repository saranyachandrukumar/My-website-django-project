from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    dob = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname
