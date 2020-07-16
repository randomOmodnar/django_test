from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import render


# 显示所有'投票问题'列表
def index(request):
    """render: 载入模板， 填充上下文"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(requests, question_id):
    return HttpResponse('you are looking at the results of question %s' % question_id)


def vote(requests, question_id):
    return HttpResponse('you are voting on question %s' % question_id)
