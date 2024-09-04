from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
# Create your models here.

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField( max_length=200)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='notes'
        verbose_name_plural='notes'
        
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subject = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished=models.BooleanField(default=False)
    due = models.DateTimeField()
    due = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title
    
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    is_finished=models.BooleanField(default=False)
    class Meta:
        verbose_name='todos'
        verbose_name_plural='todo'
    def __str__(self):
        return self.title 