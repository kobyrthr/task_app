from django import views
from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home.as_view(), name="home"),
        path('about/',views.About.as_view(), name="about")

]