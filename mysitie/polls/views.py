from django.http import HttpResponse

from django.shortcuts import render
from .models import Question


def index(request):
    lastest_question_list= Question.objects.order_by('-pub_date')[:5]
    context={ 'latest_question_list':  lastest_question_list }
    return render(request, 'polls/index.html', context)
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list': latest_question_list,
    }
    #output= ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))'''

def detail(request, question_id):
    return HttpResponse("You are looking at question %s.")

def results(request, question_id):
    response="You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)
    # Create your views here.
