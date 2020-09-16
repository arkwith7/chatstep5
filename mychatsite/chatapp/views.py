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
    template = loader.get_template('chatapp/base_contents_kr.html')
    # template = loader.get_template('chatapp/base_mycareer_kr.html')
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
    context = {
        'login_success' : False,
        'initMessages' : ["아크위드 채팅 홈페이지에 오신것을 환영합니다",
                          "아크위드 홈페이지 설명 챗봇이 회사의  vision, mission, 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    # context = {
    #     'login_success' : False,
    #     'initMessages' : ["인공지능 기반 업무자동화 RPA 컨설턴트 직무를 찾고 있는 홍길동입니다.",
    #                       "귀사를 위한 업무자동화 서비스 제공자로서 준비된 저의 역량을 소개해 드리겠습니다."]
    # }
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
