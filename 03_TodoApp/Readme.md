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
