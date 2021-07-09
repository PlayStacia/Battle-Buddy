from django.urls import path
from . import views

app_name= "battlebuddyapp"
urlpatterns = [
    
    path('', views.battlebuddyapp, name='battlebuddyapp'),
    path('getbattles/', views.getbattles, name='getbattles'),
    path('savebattle/', views.savebattle, name='savebattle')  

]