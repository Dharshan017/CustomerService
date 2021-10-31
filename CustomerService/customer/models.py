from django.db import models

# Create your models here.

class CustomerDetails(models.Model):
    firstName = models.CharField(max_length=30) 
    lastName = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30)
    mobileNo = models.IntegerField(blank=True)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.firstName+" "+self.lastName
