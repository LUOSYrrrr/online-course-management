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