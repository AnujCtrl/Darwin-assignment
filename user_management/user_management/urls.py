"""
URL configuration for user_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# user_management/urls.py
from django.urls import include, path
from users.views import create_customer, login, select_all_customers

urlpatterns = [
    path('api/customers/create', create_customer, name='create_customer'),
    path('api/customers/login', login, name='login'),
    path('api/customers/select_all', select_all_customers,
         name='select_all_customers'),
    path('frontend/', include('frontend.urls')),
]
