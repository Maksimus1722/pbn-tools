from django.urls import path
from . import view

urlpatterns = [
    path("", view.Blog.as_view(), name="blog"),
    path("<slug:category_slug>/", view.Category.as_view(), name="category"),
    path("<slug:category_slug>/<slug:slug>/", view.Article.as_view(), name="article"),
]
