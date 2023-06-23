from django.db import models

# Create your models here.
class Bank(models.Model):
    Investment_Type=models.CharField(max_length=250)
    desc=models.TextField()
    amount = models.IntegerField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Investment_Type
