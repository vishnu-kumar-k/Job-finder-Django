from django.db import models
from operator import mod

# Create your models here.
class Room(models.Model):
    job_role=models.CharField(max_length=100)
    website_link=models.CharField(max_length=100)
    com_name=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Rl_id=models.CharField(max_length=100)
    job_type=models.CharField(max_length=40)
    role=models.CharField(max_length=500)
    date=models.DateTimeField()
    img=models.ImageField(upload_to='pics')
class explore(models.Model):
    no=models.IntegerField()   
    job_tittle=models.CharField(max_length=100)
    img=models.ImageField(upload_to='explore')
    refer=models.CharField(max_length=400)
    skills=models.CharField(max_length=400)

# Create your models here.
