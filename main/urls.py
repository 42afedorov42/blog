from django.urls import path
from . import views


urlpatterns = [
    path("create/article/", views.ArticleCreateViewSet.as_view({'post': 'create'})),
    path("create/comment/", views.CommentCreateViewSet.as_view({'post': 'create'})),
    path("comment/article/<int:pk>/", views.CommentUpToL3View.as_view()),
    path("comment/l3_nested/", views.CommentNestedL3View.as_view()),
]