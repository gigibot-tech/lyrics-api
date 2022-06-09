"""GiGi_Lyrics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import include,path
from django.utils import timezone
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from core import views

admin.autodiscover()

def time(request):
    if request.user.is_authenticated:
        return JsonResponse({'now': timezone.now()})
    return HttpResponse(status=401)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('scrap.urls'))
    #path('', include('userdata.urls')),
    #path('', include('loginsystem.urls')),
    #path('auth/', include('social_django.urls', namespace='social'))
    ]
urlpatterns += staticfiles_urlpatterns()
