from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateQuestionForm, CreateCodeForm
from .models import Question, Answer, Code
from django.core.paginator import Paginator


# Create your views here.

class HomeView(TemplateView):
    template_name = 'codeisc/home_page.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = None
        all_questions = Question.objects.all().order_by('-id')
        if str(self.request.user) != "AnonymousUser":
            username = self.request.user.username
            user_codes = Code.objects.filter(author__username=username).order_by('-created_at')
            user_questions = Question.objects.filter(author__username=username).order_by('-created_at')
            last_user_code_id = user_codes.first().id
            last_user_question_id = user_questions.first().id
            last_code = reverse("CodePage", args=[last_user_code_id])
            last_question = reverse("QuestionPage", args=last_user_question_id)
            context['user'] = self.request.user
            context['last_code'] = last_code
            context['last_question'] = last_question
        context['questions'] = all_questions
        return context


class CodeView(TemplateView):
    template_name = 'codeisc/code_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        code_id = self.kwargs['codeID']
        context['code'] = Code.objects.filter(id=code_id)
        return context


class CodeCreateView(CreateView, LoginRequiredMixin):
    model = Code
    form_class = CreateCodeForm
    template_name = 'codeisc/create_code_page.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('code_detail', kwargs={'pk': self.object.pk})


class QuestionView(TemplateView):
    template_name = 'codeisc/question_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        question_id = kwargs['questionID']
        answer_id = kwargs['answerID'] or None
        context['question'] = Question.objects.filter(id=question_id)
        if answer_id:
            context['selected_answer'] = Answer.objects.filter(id=answer_id)
        return context


class QuestionCreateView(CreateView, LoginRequiredMixin):
    model = Question
    form_class = CreateQuestionForm
    template_name = 'codeisc/create_question_page.html'
    success_url = reverse_lazy('question_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionsListView(ListView):
    model = Question
    template_name = "codeisc/questions_page.html"
    context_object_name = "questions"
    ordering = "-created_at"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        user_slug = self.kwargs.get("username")
        if user_slug:
            queryset = queryset.filter(author__username=user_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class CodesListView(ListView):
    model = Code
    template_name = "codeisc/codes_page.html"
    context_object_name = "codes"
    ordering = "-created_at"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        user_slug = self.kwargs.get("username")
        if user_slug:
            queryset = queryset.filter(author__username=user_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
