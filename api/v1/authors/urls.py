from django.urls import path
from .views import AuthorDetailView, AuthorListCreateView

urlpatterns = [
    path("", AuthorListCreateView.as_view(), name="create_list_author"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="get_update_delete_author"),
]
