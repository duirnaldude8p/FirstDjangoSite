from django.db import models
#from django.contrib.postgres.fields import ArrayField

class Test2(models.Model):
    key1 = models.CharField(max_length=100)
    key2 = models.CharField(max_length=100)
    nestedArr = models.CharField(max_length=1000)

class News(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    newsComments = models.CharField(max_length=5000)
    category = models.CharField(max_length=100, null=True)
    

class Sport(models.Model):  
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    sportComments = models.CharField(max_length=5000)
    category = models.CharField(max_length=100, null=True)

class Bussiness(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    bizComments = models.CharField(max_length=5000, null=True)
    category = models.CharField(max_length=100, null=True)
   

class Account(models.Model):
    accountArr = models.CharField(max_length=10000, null=True)
    category = models.CharField(max_length=100, null=True)

class CurrentAccount(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    newsPagelikeOrDislike = models.CharField(max_length=100)
    sportPagelikeOrDislike = models.CharField(max_length=100)
    bizPagelikeOrDislike = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)























