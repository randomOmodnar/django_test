from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world????")


def detail(requests, question_id):
    return HttpResponse('you are looking at question %s'%question_id)


def results(requests, question_id):
    return HttpResponse('you are looking at the results of question %s' % question_id)


def vote(requests, question_id):
    return HttpResponse('you are voting on question %s' % question_id)