from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 用于计算结束日期（默认值为一年后）
def default_end_date():
    return now().date() + timedelta(days=365)

class UserManager(BaseUserManager):
    """自定义的用户管理器，用于创建用户和超级用户。"""

    def create_user(self, email, name, password=None, **extra_fields):
        """创建并保存一个普通用户。"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password or 'defaultpassword123')
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """创建并保存一个超级用户。"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """自定义用户模型，支持 email 作为唯一标识符。"""
    
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    date_joined = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128, default='defaultpassword123')  # 设置默认值

    USERNAME_FIELD = 'email'  # 用 email 作为唯一标识符
    REQUIRED_FIELDS = ['name', 'role']  # 创建用户时必须提供的字段

    objects = UserManager()  # 使用自定义的 UserManager

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

# 课程分类模型
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# 课程模型
class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    instructor = models.ForeignKey(
        User, limit_choices_to={'role': 'instructor'}, on_delete=models.CASCADE, related_name='courses_taught'
    )
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    description = models.TextField()
    start_date = models.DateField(default=now)  # 默认设置为当前日期
    end_date = models.DateField(default=default_end_date)  # 使用函数来计算默认值
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.instructor.name})"

# 学生课程注册模型
class Enrollment(models.Model):
    student = models.ForeignKey(
        User, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE, related_name='enrollments'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"

# 学生进度与成绩模型
class Progress(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='progress', null=True, blank=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, help_text="Progress percentage")
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.enrollment.student.name} - {self.enrollment.course.name} Progress"
