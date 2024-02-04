# pages/urls.py

from django.urls import path, include
from pages import views

#app_name = "pages"
urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("projects", include("projects.urls")),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'), 
    path('register/', views.sign_up, name='register'),
]


