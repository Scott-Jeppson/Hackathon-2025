from django.db import models

# Create your models here.
class Keyword(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.body
     
    def compare(self, text):
        return self.body in text

class CountryCodes(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.country

