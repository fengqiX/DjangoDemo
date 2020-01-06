from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from .models import Questions,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_question_list = Questions.objects.order_by('-pud_date')[:5]
#
#     # No.1 use HttpResponse() to send data to client
#     # output = ','.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#
#     # No.2 use HttpResponse() and template module to send data and page to client
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return HttpResponse(template.render(context,request))

    # No.3
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Questions.objects.order_by('-pud_date')[:5]


# def details(request, question_id):
#     # No.1 simple response
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # No.2 http404 example
#     # try:
#     #     question = Questions.objects.get(pk=question_id)
#     # except Questions.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # No.3 shortcut example
#     question = get_object_or_404(Questions,pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
    # No.4
class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'
    context_object_name='question'

# def results(request,question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Questions,pk=question_id)
#     return render(request,'polls/results.html',{'question':question,})
    # No.2


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'
    context_object_name = 'question'


def vote(request,question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Questions,pk=question_id)
    try:
        selectd_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice"
        })
    else:
        selectd_choice.votes+=1
        selectd_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))