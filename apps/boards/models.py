from django.db import models

# Create your models here.

class Boards(models.Model):
    name = models.CharField(max_length=200)
    description =models.CharField(max_length=200, blank=True, null=True)
    dete_creation = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  self.name

