from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class email_subscribe(models.Model):
    email = models.EmailField(max_length=254)
    
class course_level(models.Model):
    title = models.CharField(max_length=30)

class course(models.Model):
    title = models.CharField(max_length=50)
    level = models.ForeignKey('course_level', on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)
    description = models.CharField(default='This course is properly designed for Begineers to start python programming.', max_length=100)

class popular_course(models.Model):
    course = models.ForeignKey('course', on_delete=models.CASCADE)
    
class transaction_table(models.Model):
    t_id = models.IntegerField(default=0)
    course = models.ForeignKey('course', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

class contact_message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)