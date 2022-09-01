from email import message
from django.db import models

from apps.cards.models import Card

# Create your models here.

class Comments(models.Model):
    card_id = models.ForeignKey(Card, related_name='Commets', on_delete=models.CASCADE)
    message= models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
