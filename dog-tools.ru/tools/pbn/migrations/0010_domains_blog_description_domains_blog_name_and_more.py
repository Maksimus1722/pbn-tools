# Generated by Django 5.1.7 on 2025-03-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0009_rename_slug_category_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='domains',
            name='blog_description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='domains',
            name='blog_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='domains',
            name='blog_title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
