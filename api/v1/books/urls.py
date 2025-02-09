from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
)


urlpatterns = [
    path("", BookListCreateView.as_view(), name="create_list_Books"),
    path("<int:pk>/", BookDetailView.as_view(), name="get_update_delete_books"),
]
