from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import CreateQuestionForm, CreateCodeForm
from .models import Question, Answer, Code
from django.core.paginator import Paginator


# Create your views here.

class HomeView(TemplateView):
    template_name = 'codeisc/home_page.html'
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
    template_name = 'codeisc/code_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['codeID']
        context['code'] = Code.objects.filter(id=code_id)
        return context


class CodeCreateView(CreateView):
    model = Code
    form_class = CreateCodeForm
    template_name = 'codeisc/create_code_page.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('code_detail', kwargs={'pk': self.object.pk})


class AnswersView(TemplateView):
    template_name = 'codeisc/code_page.html'
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
    template_name = 'codeisc/code_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        question_id = kwargs['questionID']
        answer_id = kwargs['answerID'] or None
        context['question'] = Question.objects.filter(id=question_id)
        if answer_id:
            context['selected_answer'] = Answer.objects.filter(id=answer_id)
        return context


class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = 'codeisc/create_question_page.html'
    success_url = reverse_lazy('question_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
