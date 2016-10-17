"""csc394project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main/', include('main.urls')),
    url(r'^admin', admin.site.urls)
]

# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^home', views.index, name="home"),
#     url(r'^login',views.login, name="login"),
#     url(r'^register',views.register, name="register"),
#     url(r'^browse',views.coursecatalog, name="browse"),
#     url(r'^plan',views.plan, name="plan"),
#     url(r'^about',views.about, name="about"),
#     url(r'^settings',views.settings, name="settings"),
#     url(r'^admin',views.admin, name="admin")


# ]