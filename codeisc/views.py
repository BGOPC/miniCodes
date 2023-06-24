from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from .forms import CreateQuestionForm, CreateCodeForm, CreateAnswerForm
from .models import Question, Answer, Code


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


class CodeView(DetailView):
    model = Code
    template_name = 'codeisc/code_page.html'
    context_object_name = "code"

    def get_object(self, queryset=None):
        code_id = self.kwargs.get("codeID")
        obj = get_object_or_404(Code, pk=code_id)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
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
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
        question_id = kwargs.get('questionID', -1)
        answer_id = kwargs.get('answerID', None)
        question = get_object_or_404(Question, pk=question_id)
        answers = Answer.objects.filter(question=question)
        context['question'] = question
        context['answers'] = answers
        context['selected_answer'] = None
        if answer_id:
            try:
                selected_answer = answers.get(pk=answer_id)
                context['selected_answer'] = selected_answer
            except Answer.DoesNotExist:
                pass

        return context


class QuestionCreateView(CreateView, LoginRequiredMixin):
    model = Question
    form_class = CreateQuestionForm
    template_name = 'codeisc/create_question_page.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        question_id = self.object.pk
        success_url = reverse('QuestionPage', args=[question_id])
        return success_url


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
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
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
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
        return context


class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'codeisc/create_answer_page.html'
    form_class = CreateAnswerForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = get_object_or_404(Question, pk=self.kwargs.get("questionID", -1))
        return super().form_valid(form)

    def get_success_url(self):
        answer_id = self.object.pk
        question_id = self.object.question.pk
        success_url = reverse('AnswerPage', kwargs={"questionID": question_id, "answerID": answer_id})
        return success_url
