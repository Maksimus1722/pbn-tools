# Generated by Django 5.1.7 on 2025-03-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbn', '0003_alter_domains_favicon_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_preview',
            field=models.CharField(default='', max_length=800, verbose_name='Текст-превью'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_preview',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Картинка-превью'),
        ),
    ]
