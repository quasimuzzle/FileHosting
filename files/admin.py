from django.contrib import admin

from .models import File, Comment, Rating 

admin.site.register(File)
admin.site.register(Comment)
admin.site.register(Rating)

