"""
URL configuration for product_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

# myapp all urls
urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('view_product/', views.view_product, name='view_product'),
    path('pedit/ <int:pk> /', views.pedit, name='pedit'),
    path('p_edit/ <int:pk> /',views.p_edit,name='p_edit'),
    path('pdelete/ <int:pk> /',views.pdelete,name='pdelete'),
    path('search_product/',views.search_product,name='search_product'),
]
