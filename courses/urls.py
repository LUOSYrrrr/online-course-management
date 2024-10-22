from django.urls import path
from django.contrib.auth import views as auth_views  # 确保这一行导入正确
from .views import (
    CustomLoginView, signup, course_list, course_detail,
    enroll_course, progress_list
)
app_name = 'courses'  # 注册 namespace
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('', course_list, name='course_list'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('<int:course_id>/enroll/', enroll_course, name='enroll_course'),
    path('<int:course_id>/progress/', progress_list, name='progress_list'),
]