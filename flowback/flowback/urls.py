"""flowback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from . import views
from flowback.views import home, success, well_information, well_data
from django.conf import settings
from django.conf.urls.static import static

app_name = 'flowback'
urlpatterns = [
    path('home/', home.as_view(), name='home'),
    path('success/', success.as_view(), name = 'success'),
    path('well_information', well_information.as_view(), name = 'well_information'),
    #path('well_data', well_data.as_view(), name = 'inputdata'),
    #path('login/', login.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
