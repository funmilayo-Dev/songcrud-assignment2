from datetime import datetime
from email import contentmanager
from re import A
from turtle import title
from django.db import models

# Create your models here.
class Artiste(models.Model):
   first_name = models.CharField(max_length=400)
   last_name = models.CharField(max_length=400)
   age = models.IntegerField()

def __str__(self):
      return self.first_name

class Song(models.Model):
    title = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    datereleased = models.DateField(default=datetime.today)
    Artiste_id= models.IntegerField()
    likes = models.IntegerField()

def __str__(self):
      return self.title

class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.IntegerField()
    
def __str__(self):
      return self.content    