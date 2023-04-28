from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Question, Answer, Code
from django.core.paginator import Paginator


# Create your views here.

class HomeView(TemplateView):
    template_name = 'codeisc/home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        all_questions = Question.objects.all().order_by('-id')
        paginator = Paginator(all_questions, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        questions = page_obj.object_list
        context['questions'] = questions
        context['page_object'] = page_obj
        return context


class CodeView(TemplateView):
    template_name = 'codeisc/codePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['codeID']
        context['code'] = Code.objects.filter(id=code_id)
        return context


class AnswersView(TemplateView):
    template_name = 'codeisc/codePage.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        answer_list = Answer.objects.all()
        paginator = Paginator(answer_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class QuestionView(TemplateView):
    template_name = 'codeisc/codePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        question_id = kwargs['questionID']
        answer_id = kwargs['answerID'] or None
        context['question'] = Question.objects.filter(id=question_id)
        if answer:
            context['selected_answer'] = Answer.objects.filter(id=answer_id)
        return context
