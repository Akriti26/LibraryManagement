from django.contrib import admin
from django.urls import path
#from Hello.home.views import about
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("update",views.update, name='update'),
    path("delete/<int:id>/",views.delete_data, name='deletedata'),
    path("<int:id>/",views.update_data, name='updatedata'),
    
  
   
]
