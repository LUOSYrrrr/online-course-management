from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment, Progress
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.
from django.http import HttpResponse
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses:course_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def course_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # 如果未登录，重定向到登录页面
    courses = Course.objects.all()  # 获取所有课程
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user  # 获取当前用户

    # 检查用户是否为学生，并进行注册
    if user.is_authenticated and user.role == 'student':
        Enrollment.objects.get_or_create(student=user, course=course)
        return redirect('courses:course_detail', course_id=course.id)
    else:
        return redirect('courses:course_list')

@login_required
def progress_list(request):
    progress = Progress.objects.filter(enrollment__student=request.user)
    return render(request, 'courses/progress_list.html', {'progress': progress})