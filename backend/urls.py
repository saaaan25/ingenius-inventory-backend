"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('classrooms/', include('apps.classrooms.urls')),
    #path('deliveries/', include('apps.deliveries.urls')),
    #path('lists/', include('apps.lists.urls')),
    #path('notifications/', include('apps.notifications.urls')),
    #path('purchases/', include('apps.purchases.urls')),
    #path('requests/', include('apps.requests.urls')),
    #path('users/', include('apps.users.urls')),
    #path('utils/', include('apps.utils.urls')),
]
