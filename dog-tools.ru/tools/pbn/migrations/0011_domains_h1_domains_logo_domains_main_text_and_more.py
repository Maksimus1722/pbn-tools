# Generated by Django 5.1.7 on 2025-03-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0010_domains_blog_description_domains_blog_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='domains',
            name='h1',
            field=models.CharField(default='', max_length=250, verbose_name='Заголовок главной страницы'),
        ),
        migrations.AddField(
            model_name='domains',
            name='logo',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Логотип сайта'),
        ),
        migrations.AddField(
            model_name='domains',
            name='main_text',
            field=models.TextField(default='', verbose_name='Текст на главной'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='blog_description',
            field=models.CharField(default='', max_length=250, verbose_name='Description страницы блога'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='blog_name',
            field=models.CharField(default='', max_length=250, verbose_name='H1 страницы блога'),
        ),
        migrations.AlterField(
            model_name='domains',
            name='blog_title',
            field=models.CharField(default='', max_length=250, verbose_name='Title страницы блога'),
        ),
    ]
