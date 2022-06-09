from django.urls import path
from scrap import views


urlpatterns =[

    path('api/search', views.search, name='search'),
    path('api/results', views.results, name='results')
]
