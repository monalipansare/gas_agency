"""
URL configuration for taskproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/', views.HomePage,name='home'),
    path('logout/', views.LogoutPage,name='logout'),
    path('dashboard', views.DashBoard, name='dashboard'),
    path('help/', views.Help, name='help'),
    path('track-my-account/', views.TrackMyAccount, name='track_my_account'),
    path('service-request-create/', views.service_request_create, name='service_request_create')
#     path('service-requests/', views.service_request_list, name='service_request_list'),
#     path('service-requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),
#     path('service-requests/create/', views.service_request_create, name='service_request_create'),
#     path('service-requests/<int:pk>/update/', views.service_request_update, name='service_request_update'),
 ]
     #path('submit-request/', views.submit_request, name='submit_request'),



