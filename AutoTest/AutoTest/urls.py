"""AutoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from polls.views import SubjectView, show_teachers, praise_or_criticize, login, logout, get_captcha
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SubjectView.as_view()),
    path('api/subjects/', SubjectView.as_view()),
    path('api/teachers/', show_teachers),
    path('praise/', praise_or_criticize),
    path('criticize/', praise_or_criticize),
    path('login', login),
    path('logout/', logout),
    path('captcha', get_captcha),
    path('__debug__/', include(debug_toolbar.urls)),
]
