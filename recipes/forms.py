from django import forms 
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe 
        fields=['title','instructions','ingredients','image']

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User 
        fields=['username','email','password1','password2']