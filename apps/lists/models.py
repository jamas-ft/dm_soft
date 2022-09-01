from venv import create
from django.db import models

from apps.boards.models import Boards

# Create your models here.

class Lists(models.Model):
    name = models.CharField(max_length=250)
    boards_id = models.ForeignKey(Boards, related_name='lists', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
