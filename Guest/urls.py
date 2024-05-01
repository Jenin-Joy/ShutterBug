from django.contrib import admin
from django.urls import path,include
from Guest import views
app_name="webguest"

urlpatterns = [
    
    path('Logout/', views.logout_view, name='Logout'),

    path('ModelRegistration/', views.modelreg,name="ModelRegistration"),
    path('EditorRegistration/', views.editorreg,name="EditorRegistration"),
    path('PhotographerRegistration/', views.photographerreg,name="PhotographerRegistration"),
    path('UserRegistration/', views.userreg,name="UserRegistration"),

    path('Login/', views.login,name="Login"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),

    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('single/',views.single,name="single"),

    
]