# 1. Django, Tensorflow text classification 기반 챗봇
## 1.1. 개요
홈페이지에서 채팅창을 뛰워 음성과 문자로 챗봇과 채팅하는 기능을 제공한다.

## 1.2 챗팅 어플리케이션 아키텍처 주요 구성요소
파이썬 장고 웹 프레임워크를 사용하여 사용자 인터페이스를 제공하고,
채팅창으로부터 질문을 음성인식 또는 문자입력을 받아 텐서플로우를 이용 제작한
질문의도 파악, 답변작성 엔진을 통해 답변을 생성하여 채팅칭으로 반환한다.
- Django(장고) 프로젝트명 : mychatsite
- Django(장고) 프로젝트명의 앱명 : chatapp
- 채팅엔진 훈련 프로그램 : ~\mychatsite\bot_traning.py
```
실행방법 : 
~\mychatsite>python bot_traning.py
......
........
~\mychatsite>App이름을 입력하세요: chatapp
.............
.................
```
- 의도 및 채팅 말뭉치 파일 : ~\mychatsite\chatapp\ArkChatFramework\ArkNLU\DialogIntents\intents_home_kr.json

## 1.3 챗봇 어플리케이션 작성 실행을 위한 방법
1. url처리 ~\mychatsite\chatapp\views.py에 popup_chat_home(request), call_chatbot(request) 내용 추가
2. ~\mychatsite\chatapp\templates\chatapp\에서 base_contents_kr.html의 <body>에서</footer>까지 내용을 자신의 홈페이지 내용으로 변경 적용하고 다른 이름으로(자기것, 예로서 base_mycareer_kr.html) 저장
3. ~\mychatsite\chatapp\templates\chatapp\에서 base_popup_contents_kr.html을 상속 확장한 팝업 채팅용 html작성(예로서 popup_mycareer_chatting_screen.html)
4. popup_mycareer_chatting_screen.html에서 
```
    <!-- Speech To Text, Text To Speech, Ajax통신 -->
	<script type="text/javascript" src="{% static 'chatapp/js/uiForChattingClient.js' %}"></script>

```
채팅창 메시지 표출 html태그 조작, 음성인식, 음성합성을 위한 자바스트립트 확인 
```
~\mychatsite\chatapp\static\chatapp\js\uiForChattingClient.js
```
5. ~\mychatsite\chatapp\ArkChatFramework\ArkNLU\DialogIntents\intents_home_kr.json의 내용 자신의 내용으로 변경
6. 챗팅 엔진 학습 : ~\mychatsite>python bot_traning.py

# 2. 변경 파일
## 2.1 url추가 및 챗봇엔진 부분 연결
**~\mychatsite\chatapp\views.py**
```
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# 홈페이지 대화 말뭉치 텐서플로우 딥러닝 학습모델 챗봇 연결
from chatapp.ArkChatFramework.ArkChat.chatting_home import ChattingHomepage
# 챗봇 프레임워크에서 로깅
import os
import logging

# Create your views here.
context = {}

# 챗봇 초기화
logger = logging.getLogger(__name__)
work_dir = os.path.dirname(os.path.realpath(__file__))
bot = ChattingHomepage(work_dir)

# def index(request):
#     msg = '박형식 홈페이지'
#     return render(request, 'chatapp/index.html', {'message': msg})

def index(request):
    # template = loader.get_template('chatapp/base_contents_kr.html')
    template = loader.get_template('chatapp/base_mycareer_kr.html')
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
    # template = loader.get_template('chatapp/popup_chat_home_screen.html')
    template = loader.get_template('chatapp/popup_mycareer_chatting_screen.html')
    # context = {
    #     'login_success' : False,
    #     'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
    #                       "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    # }
    context = {
        'login_success' : False,
        'initMessages' : ["인공지능 기반 업무자동화 RPA 컨설턴트 직무를 찾고 있는 홍길동입니다.",
                          "귀사를 위한 업무자동화 서비스 제공자로서 준비된 저의 역량을 소개해 드리겠습니다."]
    }
    return HttpResponse(template.render(context, request))

def call_chatbot(request):
    if request.method == 'POST':
        if request.is_ajax():
            userID = request.POST['user']
            sentence = request.POST['message']
            logger.debug("question[{}]".format(sentence))
            answer = bot.get_answer(sentence, userID)
            # answer = sentence
            logger.debug("answer[{}]".format(answer))
            return HttpResponse(answer)
    return ''
```

## 2.2 챗봇 응답 표시 부분 변경
**~\mychatsite\chatapp\static\chatapp\js\uiForChattingClient.js**
```
...........
.............
...............
function processResponse(response) { // given the final CS text, converts the parsed response from the CS server into HTML code for adding to the response holder div
	//response = replace('\n','<br>\n');
	//var botSaid = '<strong>' + botName + ':</strong> ' + response + "<br>\n";
	//var botSaid = '<strong>' + botName + ':</strong> ' + response + "<br>\n";
	var botSaid = 	'<li class="left clearfix">'
		+	'    <span class="pull-left">'
		+   '        <i class="fa fa-android" style="font-size:24px;"></i>'
		+	'    </span>'
		+	'    <div class="chat-body clearfix" id="chatBodyMessage">'
		+	'        <div class="header">'
		+	'            <strong class="primary-font">' + botName + '</strong>'
		+	'            <small class="pull-right text-muted">'
		+	'                <i class="fa fa-clock-o fa-fw"></i>' + dateToYYYYMMDD(new Date()) +  '</small>'
		+	'        </div>'
		+	'		 <div id="responseMessage" style="border: 0px solid orange; border-radius: 0px 20px 20px 20px;  margin: 5px 10px 5px 0px; padding: 10px; background: #efefef; color: #6f6f6f; float: left; border-top-left-radius: 0;">'
		+	'        <p>' + response + '</p>'
		+	'    	 </div>'
		+	'    </div>'
		+	'</li>';
	
	update(botSaid);
	speak(response);
}
........
.........
..........
```
## 2.3 의도 및 채팅 말뭉치 파일 편집
**~\mychatsite\chatapp\ArkChatFramework\ArkNLU\DialogIntents\intents_home_kr.json**
"intents"안의 리스트 객체에 {}부분에 의도 부분인 "tag", 질문 부분인 "patterns", 쳇봇 응답 부분인 "responses"를 추가한다.
```
{"intents": [
        {"tag": "greeting",
         "patterns": ["안녕", "안녕하세요", "잘 지냈어요?", "여기요", "잘 계셨어요?", "거기 누구 있어요?", "계세요", "계셔요", "좋은 날 입니다"],
         "responses": ["안녕하세요, 방문해 주셔서 감사합니다.", "다시 만나서 반가워요.", "만나서 반갑습니다", "찾아 주셔서 감사합니다", "안녕하세요, 어떻게 도와 드릴까요?"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["안녕히 계셔요.", "그럼 나중에 또 들릴께요", "나중에요", "다음에", "다음번에", "장사 잘 하세요", "돈 많이 버세요", "수고하세요", "친절한 서비스에 감사합니다."],
         "responses": ["나중에 또 오세요, 방문해 주셔서 감사합니다.", "좋은 하루 되세요.", "안녕히 가세요", "감사합니다.", "고맙습니다", "즐거운 시간 되세요"]
        },
        {"tag": "thanks",
         "patterns": ["감사", "감사합니다", "고맙습니다", "좋은 서비스 감사합니다"],
         "responses": ["감사합니다"]
        },
```
