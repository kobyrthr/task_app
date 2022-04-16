from django import views
from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home.as_view(), name="home"),
        path('about/',views.About.as_view(), name="about"),
        path('yourtasks/', views.YourTasks.as_view(),name="yourtasks"),
        path('yourtasks/new', views.TaskCreate.as_view(),name="taskcreate")
]

