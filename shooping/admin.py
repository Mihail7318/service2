from django.contrib import admin
from . models import Shoop,City,Street
# Register your models here.
@admin.register(Shoop)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'street', 'home', 'open_time', 'close_time']

@admin.register(City)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Street)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name',]