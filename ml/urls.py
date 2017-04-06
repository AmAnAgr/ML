"""ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import (

					home_view, # first page to be displayed
                    google_seach_verify, # making site visible on google search.
	)

urlpatterns = [
    url(r'^google55865d30d084df3d',google_seach_verify, name="google-search"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home' ),
    url(r'^(?P<topic>.*)$', home_view, name='next'),
]
