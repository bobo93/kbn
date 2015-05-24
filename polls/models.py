import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text





class Personnel(models.Model):
    user = models.ForeignKey('auth.User')
    tel=models.IntegerField()
    dateOfBirth = models.DateTimeField()
    address=models.CharField(max_length=200)
    accountNumber=models.IntegerField()
    PESEL=models.IntegerField()
    education=models.CharField(max_length=2000)
    role=models.CharField(max_length=200)


class LocalMy(models.Model):

    address=models.CharField(max_length=200)
    numberOfRooms=models.IntegerField()
    size=models.IntegerField()
    equipment=models.CharField(max_length=200)
    propertyDescription=models.CharField(max_length=2000)
    parking=models.CharField(max_length=200)

    def __str__(self):
        return self.address



class Buyer(models.Model):
    user = models.ForeignKey('auth.User')
    tel=models.IntegerField()
    numberOfRoomsMin=models.IntegerField()
    numberOfRoomsMax=models.IntegerField()
    city=models.CharField(max_length=200)
    propertyDescription=models.CharField(max_length=2000)
    numberOfBathrooms=models.IntegerField()
    priceMax=models.IntegerField()




class Offer(models.Model):
    local=models.ForeignKey(LocalMy)
    seller=models.ForeignKey('auth.User')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    avaible=models.CharField(max_length=200)
    offerStatus=models.CharField(max_length=200)
    city=models.CharField(max_length=200)

class Bucket(models.Model):
    buyerUsername = models.CharField(max_length=200)
    offer=models.ForeignKey(Offer)




class Flat(models.Model):
    local=models.ForeignKey(LocalMy)
    elevator=models.BooleanField()
    balcony=models.BooleanField()

class Another(models.Model):
    local=models.ForeignKey(LocalMy)
    description=models.CharField(max_length=2000)


class Office(models.Model):
    local=models.ForeignKey(LocalMy)
    elevator=models.BooleanField()
    security=models.CharField(max_length=2000)

class Home(models.Model):
    local=models.ForeignKey(LocalMy)
    gardenSize=models.IntegerField()
    numberOfBalcony=models.IntegerField()
