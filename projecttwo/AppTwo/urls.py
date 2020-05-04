from django.conf.urls import include
from django.urls import path
from AppTwo import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('myform/', views.myform_view, name='myform')
]
