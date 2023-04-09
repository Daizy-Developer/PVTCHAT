from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatRoom(models.Model):
    Name =  models.CharField(max_length=30)
    Created_by =  models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
