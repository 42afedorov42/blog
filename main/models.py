from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    """Article"""
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    """Comment"""
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    article = models.ForeignKey(
                        Article, 
                        on_delete=models.CASCADE,
                        related_name='comment'
                    )
    parent = TreeForeignKey(
                'self',
                on_delete=models.CASCADE,
                null=True, blank=True,
                related_name='children'
            )

    def __str__(self):
        return self.name
