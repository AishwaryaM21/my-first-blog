from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name='post_list'),
    #Assigning a view called post_list to the root URL
]