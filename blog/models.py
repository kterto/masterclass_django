from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='título')
    body = models.TextField(verbose_name='corpo')
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='criado em')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='created_posts',
        verbose_name='criado por'
    )
    published_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name='publicado em',
    )
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='published_posts',
        verbose_name='publicado por',
    )

    class Meta:
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'

    def __str__(self):
        return self.title
