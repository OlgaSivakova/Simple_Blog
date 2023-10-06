from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Post, Comments, Director, Dressingroom, Movie, Actor

# Register your models here.
User = get_user_model()
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Dressingroom)

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
    
   
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','post')
    
