from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


    
class Recipe(models.Model):
    title=models.CharField(max_length=200)
    instructions=models.TextField()
    ingredients=models.TextField(default='Hello')
    image=models.ImageField(upload_to='recipes/',blank=True,null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title 
    
class Favorite(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        unique_together=['user','recipe']