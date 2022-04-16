from django.db import models

# Create your models here.
PRIORITY =  (
    ("hp","high"),
    ("mp","medium"),
    ("lp","low")
)

LEVEL_OF_EFFORT =  (
    ("he","high"),
    ("me","medium"),
    ("le","low")
)

STATUSES = (
    ("0","To-do"),
    ("1","Done")
)

class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.CharField(max_length=25,choices = PRIORITY)
    effort = models.CharField(max_length=25,choices = LEVEL_OF_EFFORT)
    status = models.CharField(max_length=25,choices = STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['status']