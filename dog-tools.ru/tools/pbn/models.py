import datetime
from django.db import models
from pytils.translit import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinLengthValidator, FileExtensionValidator


# Create your models here.
class Domains(models.Model):
    domain = models.CharField(
        max_length=100,
        verbose_name="Домен",
        help_text="Строго вида site.ru",
        unique=True,
    )
    title = models.CharField(
        max_length=250, default="", verbose_name="Title главной страницы"
    )
    description = models.CharField(
        max_length=500,
        default="",
        verbose_name="Meta-description главной страницы",
    )
    keywords = models.CharField(
        max_length=500, default="", verbose_name="Meta-keywords главной страницы"
    )
    h1 = models.CharField(
        max_length=250, default="", verbose_name="Заголовок главной страницы"
    )
    main_text = RichTextUploadingField(
        verbose_name="Текст на главной",
        validators=[MinLengthValidator(300)],
        help_text="Не менее 300 символов",
    )
    logo = models.ImageField(
        upload_to="static/pbn/img",
        null=True,
        verbose_name="Логотип сайта",
        help_text="Форматы: png, jpg, jpeg",
        validators=[
            FileExtensionValidator(
                allowed_extensions=(
                    "png",
                    "jpg",
                    "jpeg",
                )
            )
        ],
    )
    favicon = models.ImageField(
        upload_to="static/pbn/favicons",
        null=True,
        verbose_name="favicon",
        help_text="фавикон в формате .ico",
        validators=[FileExtensionValidator(allowed_extensions=("ico",))],
    )
    blog_title = models.CharField(
        max_length=250, default="", verbose_name="Title страницы блога"
    )
    blog_description = models.CharField(
        max_length=500, default="", verbose_name="Description страницы блога"
    )
    blog_keywords = models.CharField(
        max_length=250, default="", verbose_name="Meta-keywords страницы блога"
    )
    blog_name = models.CharField(
        max_length=250, default="", verbose_name="H1 страницы блога"
    )

    class Meta:
        verbose_name = "Домен"
        verbose_name_plural = "Домены"

    def __str__(self):
        return f"{self.domain}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    title = models.CharField(max_length=250, default="", verbose_name="Title")
    description = models.CharField(
        max_length=500,
        default="",
        verbose_name="Meta-description",
    )
    h1 = models.CharField(max_length=250, default="", verbose_name="Заголовок H1")
    domain = models.ForeignKey(
        Domains,
        on_delete=models.PROTECT,
        verbose_name="Домен",
    )
    keywords = models.CharField(
        max_length=250, default="", verbose_name="Meta-keywords"
    )
    category_slug = models.SlugField(
        max_length=100,
        null=False,
        db_index=True,
        verbose_name="URL",
        help_text="При создании поставьте любой символ. Поле заполнится автоматически.",
    )
    sort = models.IntegerField(
        default=100,
        verbose_name="Сортировка",
        help_text="Чем ближе к нулю,тем выше",
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.category_slug = slugify(self.name)[:100]
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("category", args=[self.slug])

    def __str__(self):
        return f"{self.domain} | {self.name}"

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ["-domain", "-name"]


class Article(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    domain = models.ForeignKey(
        Domains,
        on_delete=models.PROTECT,
        verbose_name="Домен",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        default="",
    )
    title = models.CharField(max_length=250, verbose_name="Title")
    description = models.CharField(max_length=500, verbose_name="Meta-description")
    keywords = models.CharField(
        max_length=500, default="", verbose_name="Meta-keywords"
    )
    slug = models.SlugField(
        max_length=100,
        null=False,
        db_index=True,
        verbose_name="URL",
        help_text="При создании поставьте любой символ. Поле заполнится автоматически.",
    )
    img_preview = models.ImageField(
        upload_to="static/pbn/img",
        null=True,
        verbose_name="Картинка-превью",
        validators=[
            FileExtensionValidator(
                allowed_extensions=(
                    "png",
                    "jpg",
                    "jpeg",
                )
            )
        ],
    )
    text_preview = models.TextField(
        max_length=300,
        verbose_name="Текст-превью",
        default="",
        help_text="Не более 300 символов вместе с пробелами",
    )
    created = models.DateField(
        default=datetime.datetime.now(), verbose_name="Дата создания"
    )
    text = RichTextUploadingField(
        verbose_name="Содержание статьи",
        validators=[MinLengthValidator(300)],
        help_text="Не менее 300 символов",
    )
    active = models.BooleanField(default=True, verbose_name="Активность")

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)[:100]
        super(Article, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("arcticle", args=[self.slug])

    def __str__(self):
        return f"{self.name}"


class OtherPage(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    domain = models.ForeignKey(
        Domains,
        on_delete=models.PROTECT,
        verbose_name="Домен",
    )
    slug = models.SlugField(
        max_length=100,
        null=False,
        db_index=True,
        verbose_name="URL",
        help_text="При создании поставьте любой символ. Поле заполнится автоматически.",
    )
    title = models.CharField(max_length=250, default="", verbose_name="Title")
    description = models.CharField(
        max_length=500,
        default="",
        verbose_name="Meta-description",
    )
    keywords = models.CharField(
        max_length=250, default="", verbose_name="Meta-keywords"
    )
    h1 = models.CharField(max_length=250, default="", verbose_name="Заголовок H1")
    text = RichTextUploadingField(verbose_name="Содержание", default="")
    sort = models.IntegerField(
        default=100,
        verbose_name="Сортировка",
        help_text="Чем ближе к нулю,тем выше",
    )

    class Meta:
        verbose_name = "Страницу"
        verbose_name_plural = "Другие страницы"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)[:100]
        super(OtherPage, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("page", args=[self.slug])

    def __str__(self):
        return f"{self.name}"


class MembransLinks(models.Model):
    domain = models.ForeignKey(
        Domains,
        on_delete=models.PROTECT,
        verbose_name="Домен",
    )
    slug_user = models.SlugField(
        max_length=100,
        null=False,
        db_index=True,
        verbose_name="URL-прокладки",
        help_text="Символный код ссылки-прокладки. Только латиница в нижним регистре и тире. Например: my-new-link",
    )
    link_money_site = models.CharField(
        max_length=150,
        verbose_name="URL Money Site",
        help_text="URL финальной страницы на Money Site",
    )

    class Meta:
        verbose_name = "Набор"
        verbose_name_plural = "Ссылки-прокладки"

    def __str__(self):
        return f"{self.slug_user}"
