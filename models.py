from django.db import models

# Create your models here.
class product(models.Model):
    name=models.TextField()
    price=models.TextField()
    mfg=models.TextField(default="non experiable")