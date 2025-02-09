from django.urls import path
from .views import UserRatingListCreateView, UserRatingDetailView

urlpatterns = [
    path(
        "",
        UserRatingListCreateView.as_view(),
        name="create_list_user_rating",
    ),
    path(
        "<int:pk>/",
        UserRatingDetailView.as_view(),
        name="get_update_delete_rating",
    ),
]
