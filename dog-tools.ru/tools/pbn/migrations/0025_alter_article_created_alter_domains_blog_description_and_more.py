# Generated by Django 5.1.7 on 2025-03-30 06:47

import ckeditor_uploader.fields
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0024_alter_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2025, 3, 30, 9, 47, 31, 935091), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='blog_description',
            field=models.CharField(default='', max_length=500, verbose_name='Description страницы блога'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='description',
            field=models.CharField(default='', max_length=500, verbose_name='Meta-description главной страницы'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='domain',
            field=models.CharField(help_text='Строго вида site.ru', max_length=100, unique=True, verbose_name='Домен'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='favicon',
            field=models.ImageField(help_text='фавикон в формате .ico', null=True, upload_to='static/pbn/favicons', validators=[django.core.validators.FileExtensionValidator(allowed_extensions='ico')], verbose_name='favicon'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='logo',
            field=models.ImageField(null=True, upload_to='static/pbn/img', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Логотип сайта'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='main_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(validators=[django.core.validators.MinLengthValidator(300)], verbose_name='Текст на главной'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='title',
            field=models.CharField(default='', max_length=250, verbose_name='Title главной страницы'),
        ),
    ]
