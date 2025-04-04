# Generated by Django 5.1.7 on 2025-03-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0013_otherpage_description_otherpage_h1_otherpage_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(default='', max_length=500, verbose_name='Meta-keywords'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(default='', max_length=250, verbose_name='Meta-keywords'),
        ),
        migrations.AddField(
            model_name='category',
            name='sort',
            field=models.IntegerField(default=100, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='domains',
            name='blog_keywords',
            field=models.CharField(default='', max_length=250, verbose_name='Meta-keywords'),
        ),
        migrations.AddField(
            model_name='otherpage',
            name='keywords',
            field=models.CharField(default='', max_length=250, verbose_name='Meta-keywords'),
        ),
        migrations.AddField(
            model_name='otherpage',
            name='sort',
            field=models.IntegerField(default=100, verbose_name='Сортировка'),
        ),
    ]
