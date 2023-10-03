from django.db import models

class Address(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    def __str__(self):
        return self.name