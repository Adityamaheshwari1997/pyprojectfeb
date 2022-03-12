from app1.views import xyz
from app1.views import signIn
from app1.views import signUp
from app1.views import logIn
from app1.views import otpVerification

"""pyprojectfeb URL Configuration

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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xyz/', xyz),
    path('signIn/', signIn),
    path('signUp/', signUp),
    path('logIn/', logIn),
    path('otpVerification/', otpVerification),
]
