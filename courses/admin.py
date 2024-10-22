from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import  User, Category, Course, Enrollment, Progress
from django.contrib.auth.views import LoginView
# 自定义 User 模型展示
class UserAdmin(BaseUserAdmin):
    # 定制显示的字段
    list_display = ('email', 'name', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    # 定制编辑界面的字段
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'role')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # 定制新增用户界面的字段
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)

# 注册自定义 User 模型
admin.site.register(User, UserAdmin)

# 自定义 Course 模型展示
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'instructor', 'start_date', 'end_date')
    list_filter = ('category', 'instructor', 'start_date')
    search_fields = ('name', 'description')

# 自定义 Category 模型展示
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# 自定义 Enrollment 模型展示
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course', 'enrolled_at')
    search_fields = ('student__name', 'course__name')

# 自定义 Progress 模型展示
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'progress', 'grade')
    list_filter = ('grade',)
    search_fields = ('enrollment__student__name', 'enrollment__course__name')
  
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/courses/')