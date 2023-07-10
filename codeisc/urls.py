from django.urls import path
from django_select2.views import AutoResponseView

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("codes/<slug:username>", views.CodesListView.as_view(), name="UserCodes"),
    path("codes/code/<int:codeID>", views.CodeView.as_view(), name="CodePage"),
    path("codes/code/new", views.CodeCreateView.as_view(), name="CreateCode"),
    path("questions/question/<int:questionID>", views.QuestionView.as_view(), name="QuestionPage"),
    path("questions/question/<int:questionID>/<int:answerID>", views.QuestionView.as_view(), name="AnswerPage"),
    path("questions/<slug:username>", views.QuestionsListView.as_view(), name="UserQuestions"),
    path("questions/question/new", views.QuestionCreateView.as_view(), name="CreateQuestion"),
    path("questions/question/<int:questionID>/create", views.AnswerCreateView.as_view(), name="CreateAnswer"),
    path("search/", views.SearchFormView.as_view(), name="search"),
    path("search/<str:query>", views.SearchResultView.as_view(), name="searchQuery"),
    path('select2/', AutoResponseView.as_view(), name='django_select2'),
]
