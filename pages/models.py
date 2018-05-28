from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Pages(models.Model):
    class Meta:
        verbose_name = 'Pages'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=100, blank=False, verbose_name='Title')
    slug = models.SlugField(max_length=180, blank=False)
    text = RichTextUploadingField()
    seo_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Seo title')
    seo_description = models.TextField(null=True, blank=True, verbose_name='Seo title')

    def __str__(self):
        return self.title
