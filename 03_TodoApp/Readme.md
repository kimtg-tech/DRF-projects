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
django-admin startproject mytodo .

-- photo 폴더 생성
python manage.py startapp todo

-- 서버 실행
python manage.py runserver


-- todo 프로젝트 설정하기
```python
INSTALLED_APPS = [
    ...
    'todo',
]
```

-- migration 수행 (db.sqlite3에 작업됨)
python manage.py migrate

-- 127.0.0.1:8000/admin 접속후 계정 만들기
python manage.py createsuperuser
(명령어 수행후 계정,비밀번호 입력후 생성)



가상환경 pip (가상환경 활성화 하고 실행)
pip freeze > requirements.txt


### 1. **실행 명령어`requirements.txt`**
아래 명령어를 사용하여 에 정의된 라이브러리를 설치합니다: `requirements.txt`
``` bash
pip install -r requirements.txt
```
### 2. **설치 후 확인**
설치 후, 아래 명령어로 설치된 패키지들이 제대로 반영되었는지 확인할 수 있습니다:
``` bash
pip freeze
```


model 생성
```python

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

db 마이그레이션
```python
python manage.py makemigrations
python manage.py migrate
```

admin.py와 urls.py에 Todo 지정하면 admin에서 입력 가능해짐


Todo 전체조회 기능 만들기

