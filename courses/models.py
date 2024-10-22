from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registered_courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"