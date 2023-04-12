from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("codes/<int:codeID>", views.CodeView.as_view(), name="code")
]
