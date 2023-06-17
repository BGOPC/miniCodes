from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("codes/code/<int:codeID>", views.CodeView.as_view(), name="CodePage"),
    path("answers/", views.QuestionView.as_view(), name="AnswersPage"),
    path("questions/question/<int:questionID>/<int:answerID>", views.QuestionView.as_view(), name="AnswerPage"),
    path("questions/question/<int:questionID>", views.QuestionView.as_view(), name="QuestionPage"),
    path("questions/<slug:username>", views, name="UserQuestions"),
    path("codes/<slug:username>", views, name="UserCodes")
]
# TODO: Implement the views for Questions And Codes For Specific User
