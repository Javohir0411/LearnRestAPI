from django.urls import path
from .views import MovieListAPIView, MovieDetailView, MovieCreateAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
    path('create/', MovieCreateAPIView.as_view()),
]
