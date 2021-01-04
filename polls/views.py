import math

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.forms import MyPersonModelForm, PythagoreanTheoremFrom

from .models import Choice, MyPerson, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))


def contact_form(request):
    gip = None
    if request.method == "GET":
        form = PythagoreanTheoremFrom()
    else:
        form = PythagoreanTheoremFrom(request.POST)
        if form.is_valid():
            first_leg = form.cleaned_data['first_leg']
            second_leg = form.cleaned_data['second_leg']
            gip = math.sqrt(pow(first_leg, 2) + pow(second_leg, 2))
    return render(
        request,
        "polls/template.html",
        context={
            "form": form,
            "gip": gip
        }
    )


def Authorization_modelform(request):
    person_new = None
    if request.method == "GET":
        form = MyPersonModelForm()
    else:
        form = MyPersonModelForm(request.POST)
        if form.is_valid():
            person_new = form.save()
            return redirect('polls:person')
    return render(
        request,
        "polls/template2.html",
        context={
            "form": form,
            "person_new": person_new
        }
    )


def output_personal_data(request, id):
    if request.method == "GET":
        pn = get_object_or_404(MyPerson, id=id)
        form = MyPersonModelForm(instance=pn)
    else:
        pn = get_object_or_404(MyPerson, id=id)
        form = MyPersonModelForm(request.POST, instance=pn)
        if form.is_valid():
            form.save()
    return render(
        request,
        "polls/template3.html",
        context={
            "pn": pn,
            "form": form,
        }
    )
