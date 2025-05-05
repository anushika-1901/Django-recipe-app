from django.shortcuts import render,redirect,get_object_or_404
from .forms import RecipeForm,RegisterForm
from django.contrib.auth.decorators import login_required

from .models import Recipe,Favorite 

from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    recipes=Recipe.objects.all()
    favorite_ids=[]
    if request.user.is_authenticated:
        favorite_ids=Favorite.objects.filter(user=request.user).values_list('pk',flat=True)
    return render(request,'home.html',{'recipes':recipes,'favorite_ids':favorite_ids})

@login_required
def my_recipes(request):
    recipes=Recipe.objects.filter(created_by=request.user)
    return render(request,'my_recipes.html',{'recipes':recipes})

@login_required
def create_recipe(request):
    if request.method=='POST':
        form=RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe=form.save(commit=False)
            recipe.created_by=request.user
            recipe.save()
            return redirect('home')
    else:
        form=RecipeForm()
    return render(request,'create_recipe.html',{'form':form})


@login_required
def update_recipe(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk,created_by=request.user)
    form=RecipeForm(request.POST or None,request.FILES or None,instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('my_recipes')
    return render(request,'create_recipe.html',{'form':form})

@login_required
def delete_recipe(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk,created_by=request.user)
    recipe.delete()
    return redirect('my_recipes')



@login_required
def toggle_favorite(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    favorite,created=Favorite.objects.get_or_create(user=request.user,recipe=recipe)
    if not created:
        favorite.delete()
    return redirect('home')

@login_required
def favorite_recipes(request):
    favorites=Favorite.objects.filter(user=request.user)
    return render(request,'favorites.html',{'favorites':favorites})

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
    
        
def login_view(request):
    if request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('my_recipes')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
