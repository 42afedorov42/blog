from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import (
    ArticleCreateSerializer,
    CommentCreateSerializer,
    ArticleCommentsSerializer,
    NestedCommentL3Serializer
)


class ArticleCreateViewSet(viewsets.ModelViewSet):
    """Adding article"""
    serializer_class = ArticleCreateSerializer


class CommentCreateViewSet(viewsets.ModelViewSet):
    """Adding comment"""
    serializer_class = CommentCreateSerializer


class CommentUpToL3View(APIView):
    """Show article comments up to 3 nesting levels. Countdown levels from 0."""
    def get(self, request, pk):
        comment = Comment.objects.filter(article_id=pk, level__lte=3)
        serializer = ArticleCommentsSerializer(comment, many=True)
        return Response(serializer.data)


class CommentNestedL3View(APIView):
    """List of nested comments level 3. Countdown levels from 0."""
    def get(self, request):
        comment = Comment.objects.filter(level=4).get_cached_trees()
        serializer = NestedCommentL3Serializer(comment, many=True)
        return Response(serializer.data)
