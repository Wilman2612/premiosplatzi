from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
   list = Question.objects.all()
   return render(request, 'polls/index.html', {
      'latest_question_list' : list
      })

def detail(request,question_id):
   obj= get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {
      'question' : obj
      })

def results(request,question_id):
   return HttpResponse(f"Estás viendo los resultados de la pregunta número{question_id}")

def vote(request,question_id):
   return HttpResponse(f"Estás votandoala pregunta número{question_id}")