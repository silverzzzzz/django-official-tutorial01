from django.contrib import admin
#add
from .models import Question

# Register your models here.
admin.site.register(Question)