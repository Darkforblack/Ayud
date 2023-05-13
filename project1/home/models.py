from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    subject = models.CharField(max_length=255)
    message= models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    