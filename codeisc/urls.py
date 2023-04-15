from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("codes/code/<int:codeID>", views.CodeView.as_view(), name="codePage"),
    path("answers/answer/<int:answerID>", views.AnswerView.as_view(), name="AnswerPage"),
    path("questions/question/<int:questionID>", views.QuestionView.as_view(), name="QuestionPage")
]
