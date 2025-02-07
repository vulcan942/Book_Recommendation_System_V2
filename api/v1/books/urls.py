from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    AuthorListCreateView,
    AuthorDetailView,
    GenreListCreateView,
    GenreDetailView,
    UserRatingListCreateView,
    UserRatingDetailView,
)


urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="create_list_author"),
    path(
        "authors/<int:pk>", AuthorDetailView.as_view(), name="get_update_delete_author"
    ),
    path("genre/", GenreListCreateView.as_view(), name="create_list_genre"),
    path("genre/<int:pk>", GenreDetailView.as_view(), name="get_update_delete_genre"),
    path(
        "user-ratings/",
        UserRatingListCreateView.as_view(),
        name="create_list_user_rating",
    ),
    path(
        "user-ratings/<int:pk>",
        UserRatingDetailView.as_view(),
        name="get_update_delete_rating",
    ),
    path("books/", BookListCreateView.as_view(), name="create_list_Books"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="get_update_delete_books"),
]
