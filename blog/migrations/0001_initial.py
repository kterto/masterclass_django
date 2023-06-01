# Generated by Django 4.2.1 on 2023-05-31 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('body', models.TextField(verbose_name='corpo')),
                ('is_premium', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(verbose_name='criado em')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='publicado em')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_posts', to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('published_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='published_posts', to=settings.AUTH_USER_MODEL, verbose_name='publicado por')),
            ],
        ),
    ]
