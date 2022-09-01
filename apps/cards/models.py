from django.db import models
from apps.lists.models import Lists


# Create your models here.


class Card(models.Model):
    name= models.CharField(max_length=200)
    lists_id = models.ForeignKey(Lists, related_name='Card', default=0, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add= True)
    expirate_date = models.DateField()
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.name


