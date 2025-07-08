"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from filebrowser.sites import site

# from . import settings


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # path('iyanuashiri/', admin.site.urls),
    # path('iyanuashiri/filebrowser/', site.urls),
    path('', include('meethub.events.urls'), name='events'),
    
    path('', include('meethub.accounts.urls')),
    # path('tinymce/', include('tinymce.urls')),
    path('', include('meethub.profile.urls'), name='profile'),
    path('', include('meethub.actions.urls')),
    path('', include('meethub.comments.urls')),

    # path('api/v1/', include('apiv1.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)