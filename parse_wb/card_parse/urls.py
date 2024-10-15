from django.urls import path

from .views import CardDataListView, ParseArticle

urlpatterns = [
    path(
        "parse-article/<str:article>/",
        ParseArticle.as_view(),
        name="parse-article",
    ),
    path("card-data/", CardDataListView.as_view(), name="card-data-list"),
]
