from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Task
# Create your views here.

class Home(TemplateView):
    template_name="home.html"
class About(TemplateView):
    template_name="about.html"
class YourTasks(TemplateView):
    template_name="yourtasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context

class TaskCreate(TemplateView):
    template_name="taskcreate.html"

# class Task:
#     def __init__(self,name,priority,loe,status):
#         self.name = name
#         self.priority = priority
#         self.loe = loe
#         self.status = status
# tasks = [
# Task("Complete Finch Collector homework","High","High","In progress"),
# Task("Do the dishes","Medium","Low","Done"),
# Task("Workout","High","Medium","To do"),
# Task("Cook for the week","High","High","To do")
# ] 



  