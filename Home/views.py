from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def add_category(request):
    pass

def add_tag(request):
    pass

def upload_image(request):
    pass

def view_categories(request):
    categories = Category.objects.all()
    return render(request, "index.html", {'categories': categories})
    
    
def view_tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags}) 

def view_images(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})