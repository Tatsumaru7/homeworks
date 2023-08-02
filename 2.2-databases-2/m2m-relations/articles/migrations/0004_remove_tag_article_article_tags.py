# Generated by Django 4.2.3 on 2023-08-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_tag_name_alter_scope_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', through='articles.Scope', to='articles.tag'),
        ),
    ]
