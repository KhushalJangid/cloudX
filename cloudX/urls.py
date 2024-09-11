"""Solution_ONE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from cloudX import settings,core
from django.conf.urls.static import static

admin.site.site_header = "Cloud X"
admin.site.site_title = "Cloud X | Admin"
admin.site.index_title = "Welcome to Admin Control Pannel"

urlpatterns = [
    # path("",home,name="home"),
    path("admin/", admin.site.urls),
    path("u/",include("Accounts.urls")),
    path("",include("main.urls")),
    #path('media/<str:path>/<str:file>', core.media, name='media'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
