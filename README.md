# online-course-management



####  Django 初始化

1. 安装 Django 和 `djongo`：

   ```bash
   
   pip install django djongo
   ```

2. 创建 Django 项目：

   ```bash
   
   django-admin startproject online_course .
   ```

   

3. 在 `settings.py` 中配置 MongoDB：



```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'online_course',
        'CLIENT': {
            'host': 'mongodb+srv://luosylois:HDQNHKbMDrxhLJz1@online-course.4tn3g.mongodb.net/',
            'retryWrites': True,
            'w': 'majority',
        },
    }
}
```

### **在项目根目录下创建 App**

1. 确保你在包含 **`manage.py`** 文件的目录下运行以下命令：

   ```
   
   python manage.py startapp courses
   ```

2. 执行后，`courses` 目录将被创建，目录结构如下：

online-course-management/
├── manage.py
├── online_course_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── courses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py

### **注册 App 到 Django 项目**

1. 打开 **`settings.py`** 文件，并在 `INSTALLED_APPS` 列表中添加新建的 `courses` app：

   ```
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'courses',  # 添加你的新 app
   ]
   ```

2. 运行数据库迁移以确保项目正常：

   ```
   
   python manage.py migrate
   ```

------

### **配置 URL 路由**

1. 打开 **`courses/urls.py`**（如果没有这个文件，可以手动创建），并添加如下内容：

   ```python
   
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index, name='index'),  # 主页视图
   ]
   ```

2. 在项目的 **`online_course_management/urls.py`** 中包含新 app 的路由：

   ```urls
   
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('courses/', include('courses.urls')),  # 包含 courses app 的路由
   ]
   ```

### **重新运行服务器**

如果一切配置正确，尝试重新运行服务器：

```

python manage.py runserver
```

访问 **`http://127.0.0.1:8000/courses/`**，你应该看到：

```
css


复制代码
Welcome to the Courses App!
```

## **每个 URL 的访问说明**

### 1. **课程列表**

- **URL:** `/courses/`
- **视图函数:** `course_list`
- **功能:** 显示所有课程的列表，包括课程的名称和简介。

#### **示例：**

- **访问路径:** http://127.0.0.1:8000/courses/

- 预期结果:

  ```
  text
  
  
  复制代码
  - Introduction to Python
  - Data Structures
  - Calculus I
  ```

------

### 2. **课程详情**

- **URL:** `/courses/<course_id>/`
- **视图函数:** `course_detail`
- **功能:** 显示单个课程的详细信息，如课程描述、教师、开始和结束日期等。

#### **示例：**

- **访问路径:** http://127.0.0.1:8000/courses/1/

- 预期结果:

  ```
  vbnet
  
  
  复制代码
  Course: Introduction to Python
  Instructor: Bob
  Duration: 40 hours
  Description: Learn the basics of Python programming.
  ```

------

### 3. **注册课程**

- **URL:** `/courses/<course_id>/enroll/`
- **视图函数:** `enroll_in_course`
- **功能:** 学生注册选定的课程。

#### **示例：**

- **访问路径:** http://127.0.0.1:8000/courses/1/enroll/

- 预期结果:

  ```
  css
  
  
  复制代码
  Successfully enrolled in Introduction to Python.
  ```

------

### 4. **查看学生进度**

- **URL:** `/courses/<course_id>/progress/`
- **视图函数:** `view_progress`
- **功能:** 查看当前用户在选定课程中的学习进度和成绩。

#### **示例：**

- **访问路径:** http://127.0.0.1:8000/courses/1/progress/

- 预期结果:

  ```
  makefile
  
  
  复制代码
  Student: Alice
  Progress: 85.5%
  Grade: A
  ```

------

## **管理员后台**

- **URL:** `/admin/`
- **功能:** 管理员可以通过 Django 后台管理用户、课程和注册信息。

#### **示例：**

- **访问路径:** http://127.0.0.1:8000/admin/
- 预期结果:
  - 通过管理员账号登录，管理数据。

------

## **每个 URL 的作用总结**

| URL                              | 访问路径         | 功能描述                     |
| -------------------------------- | ---------------- | ---------------------------- |
| `/courses/`                      | 课程列表页面     | 查看所有课程                 |
| `/courses/<course_id>/`          | 单个课程详情页面 | 查看课程的详细信息           |
| `/courses/<course_id>/enroll/`   | 课程注册页面     | 学生注册课程                 |
| `/courses/<course_id>/progress/` | 学生进度页面     | 查看学生的课程学习进度和成绩 |
| `/admin/`                        | Django 管理后台  | 管理员登录并管理数据         |