# Generated by Django 5.1.7 on 2025-03-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0006_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text_preview',
            field=models.TextField(default='', max_length=800, verbose_name='Текст-превью'),
        ),
    ]
