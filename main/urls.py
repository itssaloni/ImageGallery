"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import view_categories
from Home.views import view_tags
from Home.views import view_images, upload_image, add_tag, add_category
from Home.views import delete_image

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category', view_categories, name='category'),
    path('tags', view_tags, name='tags'),
    path('', view_images, name='images'),
    
    path('image/add', upload_image, name = "upload_image"),
    path('tag/add', add_tag, name = 'add_tag'),
    path('category/add', add_category, name = "add_category"),
    
    path('image/delete/<int:id>', delete_image, name = "delete_image"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)
