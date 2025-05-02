from django.shortcuts import render,redirect,get_object_or_404
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def recipe_list(request):
    recipes=Recipe.objects.all()
    return render(request,'recipe_list.html',{'recipes':recipes})

@login_required
def recipe_add(request):
    form=RecipeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        recipe=form.save(commit=False)
        recipe.user=recipe.user
        recipe.save()
        return redirect('recipe_list')
    return render(request,'recipe_form.html',{'form':form})


@login_required
def recipe_edit(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    form=RecipeForm(request.POST or None,request.FILES or None,instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request,'recipe_form.html',{'form':form})

@login_required
def recipe_delete(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    if request.method=='POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request,'recipe_confirm_delete.html',{'recipe':recipe}) 

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('recipe_list')
    return render(request,'register.html',{'form':form})



@method_decorator(login_required,name='dispatch')
class LogoutConfirmView(TemplateView):
    template_name='logout_confirm.html'


def home(request):
    print("User :",request.user)
    print("Is authenticated",request.user.is_authenticated)
    return render(request,'home.html')


@login_required 
def toggle_favorite(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    if request.user in recipe.favorites.all():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)
    return redirect('recipe_list')


