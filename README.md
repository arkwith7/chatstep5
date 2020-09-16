# 1. Django, Tensorflow text classification 기반 챗봇
## 1.1. 개요
홈페이지에서 채팅창을 뛰워 음성과 문자로 챗봇과 채팅하는 기능을 제공한다.

## 1.2 챗팅 어플리케이션 아키텍처 주요구성요소
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
