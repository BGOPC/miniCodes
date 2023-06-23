from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("codes/<slug:username>", views.CodesListView.as_view(), name="UserCodes"),
    path("codes/code/<int:codeID>", views.CodeView.as_view(), name="CodePage"),
    path("codes/create", views.CodeCreateView.as_view(), name="CreateCode"),
    path("questions/question/<int:questionID>", views.QuestionView.as_view(), name="QuestionPage"),
    path("questions/question/<int:questionID>/<int:answerID>", views.QuestionView.as_view(), name="AnswerPage"),
    path("questions/<slug:username>", views.QuestionsListView.as_view(), name="UserQuestions"),
    path("questions/create", views.QuestionCreateView.as_view(), name="CreateQuestion"),
    path("questions/<int:questionID>/create", views.AnswerCreateView.as_view(), name="CreateAnswer")
]
