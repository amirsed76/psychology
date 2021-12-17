from django.urls import path

from . import views

urlpatterns = [
    # path('<str:room_name>/', views.room, name='room'),
    path("question", views.QuestionRetrievedAPIView.as_view()),
    path("question/<int:pk>", views.QuestionRetrievedAPIView.as_view()),
    path("participant/<str:mobile_number>/exists", views.ExistParticipant.as_view()),
    path("help/health", views.GetHealthQuestionAPIView.as_view()),
    path("help/terms", views.GetTermAPIView.as_view()),
    path("help/question_text", views.GetQuestionTextAPIView.as_view()),
    path("help/how_do_task", views.GetHowDoTaskAPIView.as_view()),
    path("register", views.TaskRegisterCreateAPIView.as_view()),
    path("generate", views.TaskInitInfoAPIView.as_view())
]
