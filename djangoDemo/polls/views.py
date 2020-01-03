from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Questions
from django.shortcuts import render


def index(request):
    latest_question_list = Questions.objects.order_by('-pud_date')[:5]
    # No.1 use HttpResponse() to send data to client
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # No.2 use HttpResponse() and template module to send data and page to client
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))

def details(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)