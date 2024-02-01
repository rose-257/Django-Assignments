from django.db import models

# Create your models here.



class student(models.Model):
    Genderchoices = [
   ('M', 'Male'),
   ('F', 'Female')
]
    
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=200,null=True)
    confirmpassword = models.CharField(max_length=200,null=True)
    gender = models.CharField(choices=Genderchoices, max_length=10)

