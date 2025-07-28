
[작업환경]
windows11, 
Pycham
Python 3.13.2
django-5.2.4

-- 가상환경 설정
python -m venv myvenv

-- 가상환경 실행 (윈도우기준)
myvenv\Scripts\activate

-- 비활성화
deactivate


-- django 설치
pip install django

-- 새로운 project 생성
django-admin startproject myweb .

-- photo 폴더 생성
python manage.py startapp photo

-- 서버 실행
python manage.py runserver


-- setting 설정 (myweb/settings.py)
INSTALLED_APPS = [
    ...
    'photo',
]

-- setting 더보기
DEBUG = True 
ALLOWED_HOST = ['127.0.0.1'] # 허용할 호스트

-- url 설정 (myweb/url.py)
urlpatterns = [
    path('admin/', admin.site.urls),
]

-> 여기까지 했으면 127.0.0.1:8000/admin 접속시 no such table: django_session 에러가 뜸

-- migration 수행 (db.sqlite3에 작업됨)
python manage.py migrate

-- 127.0.0.1:8000/admin 접속후 계정 만들기
python manage.py createsuperuser
(명령어 수행후 계정,비밀번호 입력후 생성)


-- model 입력 (photo/models.py)
```python
from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.IntegerField()
```

-- model중에 image가 있으면 pillow설치해야함
python -m pip install Pillow


-- model 적용시키기
python manage.py makemigrations
python manage.py migrate

-- model admin에 적용 (photo/admin.py)
```python
from django.contrib import admin
from .models import Photo

# Register your models here.
admin.site.register(Photo)
```

-> 이렇게 하면 model 을 django-admin 에서 crud가 가능해짐


-- template 만들기 (사진 목록 화면 만들기, photo/templates/photo) 


-- view 작성 (photo/view.py)
```python
from django.shortcuts import render

# Create your views here.
def photo_list(request):
    return render(request, 'photo/photo_list.html', {})
```

-- URL (photo/url.py)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
]
```

-- URL (myweb/url.py)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls'))
]

```


-- 이미지 처리를 위한 추가 설정 setting.py
```python
import os
# 업로드된 파일의 URL 접근 경로
MEDIA_URL = '/images/'

# 실제 파일이 저장될 경로 (BASE_DIR 기준)
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
```

-- 이미지 처리를 위한 추가 설정 myweb/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls'))
]

# 개발 서버에서 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```