"""
URL configuration for file_hosting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from files import views 
from files import upload_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.file_list, name='file_list'),
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
    path('file/add/', views.add_file, name='add_file'),
    path('file/<int:file_id>/delete/', views.delete_file, name='delete_file'),
    path('file/<int:file_id>/comment/', views.add_comment, name='add_comment'),
    path('file/<int:file_id>/rate/', views.add_rating, name='add_rating'),
    path('file/{file_id}/upload/', upload_file.upload_file, name='upload_file'),


]
