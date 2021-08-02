from rest_framework import serializers
from .models import Article, Comment


class FilterCommentSerializer(serializers.ListSerializer):
    """Comments filter. Anly parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Recursive comments list"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class NestedCommentL3Serializer(serializers.ModelSerializer):
    """List of nested comments level 3"""
    children = RecursiveSerializer(many=True)
    class Meta:
        model = Comment
        fields = ['level', 'name', 'text', 'children']


class ArticleCommentsSerializer(serializers.ModelSerializer):
    """Article comments list"""
    #children = RecursiveSerializer(many=True)
    class Meta:
        model = Comment
        fields = ['level', 'name', 'text', 'children']


class ArticleCreateSerializer(serializers.ModelSerializer):
    """Adding article"""

    class Meta:
        model = Article
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    """Adding comment"""

    class Meta:
        model = Comment
        fields = "__all__"
