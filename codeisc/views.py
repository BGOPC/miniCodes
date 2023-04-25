from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Question, Answer, Code
from django.core.paginator import Paginator


# Create your views here.

class HomeView(TemplateView):
    template_name = 'codeisc/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        latest_questions = Question.objects.all().order_by('-id')[:10]
        context['question'] = latest_questions
        return context


class CodeView(TemplateView):
    template_name = 'codeisc/codePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['codeID']
        context['code'] = Code.objects.filter(id=code_id)
        return context


class AnswerView(TemplateView):
    template_name = 'codeisc/codePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['answerID']
        context['answer'] = Code.objects.filter(id=code_id)
        return context

class QuestionView(TemplateView):
    template_name = 'codeisc/codePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['questionID']
        context['question'] = Code.objects.filter(id=code_id)
        return context