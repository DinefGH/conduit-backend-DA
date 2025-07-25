from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

# Allow both slash‑terminated AND non‑slash URLs on the ViewSet routes
router = DefaultRouter(trailing_slash='/?')
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    # this now serves:
    #   GET/POST  /articles       and  /articles/
    #   GET       /articles/{pk}  and  /articles/{pk}/
    url(r'^', include(router.urls)),

    # feed, favorites, comments and tags all accept an optional slash too
    url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',
        ArticlesFavoriteAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$',
        CommentsListCreateAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
        CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
]