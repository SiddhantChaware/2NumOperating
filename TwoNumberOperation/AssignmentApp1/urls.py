from django.urls import path

from AssignmentApp1 import views

urlpatterns =[
     path('',views.operation_fun),
    path('read_data',views.read_data)
]