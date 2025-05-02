from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


    
class Recipe(models.Model):
    title=models.CharField(max_length=200)
    instructions=models.TextField()
    ingredients=models.TextField(default='Hello')
    image=models.ImageField(upload_to='recipes/',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    favorites=models.ManyToManyField(User,related_name='favorite_recipes',blank=True)
    def __str__(self):
        return self.title 