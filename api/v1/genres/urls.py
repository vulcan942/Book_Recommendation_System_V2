from django.urls import path
from .views import GenreListCreateView, GenreDetailView

urlpatterns = [
    path("", GenreListCreateView.as_view(), name="create_list_genre"),
    path("<int:pk>/", GenreDetailView.as_view(), name="get_update_delete_genre"),
]
