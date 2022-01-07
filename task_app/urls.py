from django.urls import path

from . import views

urlpatterns = [
    path("question", views.QuestionRetrievedAPIView.as_view()),
    path("question/<int:pk>", views.QuestionRetrievedAPIView.as_view()),
    path("participant/<str:mobile_number>/exists", views.ExistParticipant.as_view()),
    path("help/health", views.GetHealthQuestionAPIView.as_view()),
    path("help/terms", views.GetTermAPIView.as_view()),
    path("help/first_page", views.GetFirstPageTextAPIView.as_view()),
    path("help/how_do_task", views.GetHowDoTaskAPIView.as_view()),
    path("register", views.TaskRegisterCreateAPIView.as_view()),
    path("generate", views.TaskInitInfoAPIView.as_view()),
    path("training_generate", views.TaskTrainingInitInfoAPIView.as_view()),
    path("apply", views.ApplyTaskCreateAPIView.as_view()),

]
