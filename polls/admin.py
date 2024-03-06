from django.contrib import admin
# Register your models here.
from .models import Contact,Blog

class CustomContact(admin.ModelAdmin):
    list_display=("Name","datetimes")

admin.site.register(Contact,CustomContact)
class CustomBlog(admin.ModelAdmin):
    list_display=("name","datetimes")
admin.site.register(Blog,CustomBlog)  