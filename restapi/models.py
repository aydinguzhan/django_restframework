from django.db import models


# Create your models here.

class Data(models.Model):
    mac = models.CharField(max_length=100)
    card = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_info = models.DateField()
    updated_info = models.DateField(auto_now_add= True)
    last_info = models.DateField(auto_now=True)

    def __str__(self):
        return self.name