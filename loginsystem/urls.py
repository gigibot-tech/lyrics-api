from django.urls import path
from loginsystem import views


urlpatterns =[

    path('/signin', views.signin, name='login'),
    path('/signup', views.signup, name='create'),
    path('/signout', views.signout, name='logout'),
    path('/contact', views.contact, name='contact'),
    path('/about', views.about, name='about'),


]
