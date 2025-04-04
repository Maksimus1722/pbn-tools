# Generated by Django 5.1.7 on 2025-03-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0014_article_active_article_keywords_category_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domains',
            name='blog_keywords',
            field=models.CharField(default='', max_length=250, verbose_name='Meta-keywords страницы блога'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='logo',
            field=models.ImageField(null=True, upload_to='static/pbn/img', verbose_name='Логотип сайта'),
        ),
    ]
