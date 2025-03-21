from django.db import models

# Create your models here.
class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.body
    
    def getScore(self):
        return self.score
     
    def compare(self, text):
        return self.body in text

class CountryCode(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.country

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    passwordHash = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)

class Phrase(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.body
    
    def getScore(self):
        return self.score

    def compare(self, text):
        return self.body in text