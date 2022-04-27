from django.db import models
#from django.contrib.auth.models import User 

class formgroup(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    date=models.DateTimeField()
    seats=models.IntegerField()

    def __str__(self):
        return self.name

class Pigga(models.Model):
    service = models.DecimalField(max_digits=6, decimal_places=2)
    

class service(models.Model):
    dishname_id = models.AutoField(primary_key=True)
    service=models.CharField(max_length=50)
    dishname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.dishname

class WorkingTime(models.Model):
    TimeWT = models.CharField(max_length=30)
    DaysWT = models.CharField(max_length=50)

    def __str__(self):
        return self.TimeWT

class Menu(models.Model):
    dishname_id = models.AutoField(primary_key=True)
    price=models.CharField(max_length=50)
    menudishname = models.CharField(max_length=50)
    menudesc = models.CharField(max_length=500)

class Chefs(models.Model):
    Chefs_id = models.AutoField(primary_key=True)
    Chefimage = models.ImageField(upload_to='images')
    Chefname = models.CharField(max_length=50)
    Chefdesc = models.CharField(max_length=500)

    def __str__(self):
        return self.Chefname

class Testmonials(models.Model):
    Testmonials_id = models.AutoField(primary_key=True)
    Testmonialsname = models.CharField(max_length=50)
    Testmonialstitle = models.CharField(max_length=50)
    Testmonialsdesc = models.CharField(max_length=200)
    Testmonialsimage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Testmonialsname

        

# Create your models here.
