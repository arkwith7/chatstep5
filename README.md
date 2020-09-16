# 1. 장고 프로젝트(mychatsite) 생성
## 1.1. 장고 프로젝트를 실행할 디렉토리로 이동합니다.
```
(chat_env) C:\Users\saint\GroupProject>cd step1
```

## 1.2 장고 프로젝트를 django-admin startproject "프로젝트명" 으로 생성
프로젝트명으로 mychatsite를 사용하여 생성
```
(chat_env) C:\Users\saint\GroupProject\step1>django-admin startproject mychatsite

(chat_env) C:\Users\saint\GroupProject\step1>dir/w
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: EA5F-25B4

 C:\Users\saint\GroupProject\step1 디렉터리

[.]          [..]         [mychatsite]
               0개 파일                   0 바이트
               3개 디렉터리  264,312,532,992 바이트 남음
```

## 1.3 생성된 프로젝트 디렉토리로 이동
```
(chat_env) C:\Users\saint\GroupProject\step1>
(chat_env) C:\Users\saint\GroupProject\step1>cd mychatsite

(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>
(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>dir/w
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: EA5F-25B4

 C:\Users\saint\GroupProject\step1\mychatsite 디렉터리

[.]          [..]         manage.py    [mychatsite]
               1개 파일                 557 바이트
               3개 디렉터리  264,312,532,992 바이트 남음
```
## 1.4 생성된 프로젝트 실행
```
(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>
(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>
(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 14 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 09, 2020 - 13:50:54
Django version 2.0.2, using settings 'mychatsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[09/Sep/2020 13:51:07] "GET / HTTP/1.1" 200 16348
[09/Sep/2020 13:51:07] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[09/Sep/2020 13:51:07] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 80304
[09/Sep/2020 13:51:07] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 82564
[09/Sep/2020 13:51:07] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 81348
```
# 2. 장고 어플리케이션(chatapp) 생성
```
(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>python manage.py startapp chatapp

(chat_env) C:\Users\saint\GroupProject\step1\mychatsite>dir/w
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: EA5F-25B4

 C:\Users\saint\GroupProject\step1\mychatsite 디렉터리

[.]          [..]         [chatapp]    db.sqlite3   manage.py    [mychatsite]
               2개 파일                 557 바이트
               4개 디렉터리  264,305,500,160 바이트 남음
```
## 2.1 장고 어플리케이션(chatapp)에서 views.py파일에 페이지 등록
**mychatsite\chatapp\views.py**
```
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
context = {}

# def index(request):
#     msg = '박형식 홈페이지'
#     return render(request, 'chatapp/index.html', {'message': msg})

def index(request):
    template = loader.get_template('chatapp/base_contents_kr.html')
#    template = loader.get_template('base_contents.html')
    context = {
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def chat_home(request):
    template = loader.get_template('chatapp/chat_home_screen.html')
    context = {
        'login_success' : False,
        'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
                          "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    return HttpResponse(template.render(context, request))

def popup_chat_home(request):
    template = loader.get_template('chatapp/popup_chat_home_screen.html')
    context = {
        'login_success' : False,
        'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
                          "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    return HttpResponse(template.render(context, request))

def call_chatbot(request):
    if request.method == 'POST':
        if request.is_ajax():
            userID = request.POST['user']
            sentence = request.POST['message']
            # logger.debug("question[{}]".format(sentence))
            # answer = clean_up_sentence(sentence)
            # answer = bot.response(sentence, userID)
            # answer = bot.get_answer(sentence, userID)
            answer = sentence
            # logger.debug("answer[{}]".format(answer))
            return HttpResponse(answer)
     
    return render(request)

```
## 2.2 장고 어플리케이션(chatapp)에 urls.py파일 생성
**mychatsite\chatapp\urls.py**
```
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat_home', views.chat_home, name='chat_home'),
    path('popup_chat_home', views.popup_chat_home, name='popup_chat_home'),
    path('call_chatbot', views.call_chatbot, name='call_chatbot'),
]
```
# 3. 프로젝트(mychatsite)에 어플리케이션(chatapp) 연결
## 3.1 settings.py에 어플리케이션(chatapp) 등록
**mychatsite\mychatsite\settings.py**
```
......
...............
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#  여기에 생성한 chatapp 어플리케이션 이름 등재
    'chatapp.apps.ChatappConfig',
]

# Templates 디렉토리 위치 등록
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
        # Template에서 사용하는 STATIC 파일관련 설정 
            'builtins': ['django.contrib.staticfiles.templatetags.staticfiles'],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

.............
................
```

# 3.2 프로젝트(mychatsite)의 urls.py에 어플리케이션(chatapp)의 urls.py 등록
**mychatsite\mychatsite\urls.py**
```
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('chatapp.urls')),
    path('chatapp/', include('chatapp.urls')),
    path('admin/', admin.site.urls),
]
```
