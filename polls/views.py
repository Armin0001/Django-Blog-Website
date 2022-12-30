from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice, Voter
from django.urls import reverse
from django.views import generic
from django.utils import timezone



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):

    template_name = 'polls/base.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def myPolls(request):
# 	return render(request, 'blog/base.html', {'title':'Polls'})
#


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # choice = get_object_or_404(Choice, pk=choice_id)
    #if Voter.objects.filter(poll_id=question_id, user_id = request.user.id).exists():
        #Redisplays the question with an error message.
        # return render(request, 'polls/detail.html', {
        #     'question': question,
        #     'error_message': "Vote already placed this particular question.",
        # })

    # def get_context_data(self, **kwargs):
    #     # context = super(IndexView, self).get_context_data(**kwargs)
    #     context = {
    #         'choice': Choice.objects.get(pk=choice_id).votes.count(),
    #         # 'questions': Question.objects.all(),
    #         'questions': Question.objects.all()
    #     }
    #     return context

    # if Voter.objects.filter(choice_id=choice_id, user_id=request.user.id).exists():
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "Sorry, but you have already voted."
    #     })

    #has_voted = request.user.choice_set.filter(question=question).exists()
    if Voter.objects.filter(poll_id=question_id, user_id=request.user.id).exists():
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Sorry, but you have already voted."
        })

    try:
        # if has_voted:
        #     return render(request, 'polls/detail.html', {
        #         'question': question,
        #         'error_message': "Sorry, you have placed a vote.",
        #     })
        # if Voter.objects.filter(poll=choice, user=request.user).exists():
        #     #messages.error(request, "Already Voted on this choice")
        #     return render(request, 'polls/detail.html', {
        #         'question': question,
        #         'error_message': "Already voted.",
        #     }),
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        v = Voter(user=request.user, poll=question)
        v.save()
        #Voter.objects.create(voter=request.user, choice=choice_id)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # Save the vote.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))