import datetime
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.template import Template


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
    question= get_object_or_404(Question, pk=question_id)
   
    return render(request, 'polls/detail.html',{'question': question})    
    #return HttpResponse("You are looking at question %s.")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        select_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesExist):
           return render(request, 'polls/detail.html',{'question': question, 'error-message': "You din't select a choice",
                                                       })
    else:
         select_choice.votes += 1
         select_choice.save()
         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    # Create your views here.
