from django.contrib import admin

# Register your models here.
from .models import Course, Student, Progress

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Progress)