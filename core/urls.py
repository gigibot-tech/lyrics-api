from django.urls import path
from core import views

urlpatterns = [
    #path('', views.artists_view),
    path('', views.home, name = 'home'),
    path(
        'sw.js',
        views.ServiceWorkerView.as_view(),
        name=views.ServiceWorkerView.name,
    ),
    path('search/', views.search, name='search'),
    path('results/', views.results, name='results')

]