#from unicodedata import name
from django.contrib import admin
from home.models import Registration
# Register your models here.

@admin.register(Registration)
class Useradmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'password')
