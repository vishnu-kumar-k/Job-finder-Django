from django.contrib import admin

from job.views import explore
from .models import Room
from .models import explore

# Register your models here. 
admin.site.register(Room)
admin.site.register(explore)