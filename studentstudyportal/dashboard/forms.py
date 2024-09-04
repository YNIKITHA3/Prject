from django import forms
from . models import *
from .models import Homework
from django.db import models
from django.forms import ModelForm



class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']
        

class DateInput(forms.DateInput):
    input_type='data'


'''class HomeWorkForm(forms.ModelForm):
    class meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']'''
        
    
    
class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="enter")
    
    
    
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']
    
    