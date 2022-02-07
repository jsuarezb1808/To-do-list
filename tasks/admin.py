from django.contrib import admin

#local app
from .models import task
# Register your models here.

#this adds the tasks to the admin site in the project
admin.site.register(task)
