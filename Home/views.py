from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def add_category(request):
    pass

def add_tag(request):
    pass

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images')
    ctx = {'form': ImageForm()}
    return render(request, "upload_image.html",ctx)

def view_categories(request):
    categories = Category.objects.all()
    return render(request, "category.html", {'categories': categories})
    
    
def view_tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags}) 

def delete_image(request, id):
    try:
       image = Image.objects.get(id=id)   
       image.delete()
    except:
        pass   
    return redirect('images')

def view_images(request):
    images = Image.objects.all()
    category = Category.objects.all()
    print("img ==>",images)
    return render(request, 'index.html', {'images': images , 'abc':category})