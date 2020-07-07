from __future__ import unicode_literals
import datetime
from django.urls import reverse
from django.db import models
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from django_markdown.models import MarkdownField
from django.contrib.postgres.fields import ArrayField
# from tinymce.models import HTMLField



fs = FileSystemStorage(location='web/media/')

# Create your models here.
class CarouselCaption(models.Model):
	caption = models.CharField(max_length=100)
	publish_date = models.DateField(auto_now=True)
	caption_no = models.IntegerField()

	def __str__(self):
		return self.caption

class About(models.Model):
	description = RichTextField()
	publish_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.description



class Resume(models.Model):
	skill_icon = models.CharField(max_length=100)
	skill = models.CharField(max_length=100)
	skill_desc = models.CharField(max_length=150)
	experienced = models.BooleanField(default=True)
	created = models.DateField(auto_now=True)

	def __str__(self):
		return self.skill

class PortfolioGraphic(models.Model):
	site_name = models.CharField(max_length=100)
	graphic = models.ImageField(storage = fs)
	site_url = models.URLField(max_length=100)
	graphic_no = models.IntegerField(unique=True)
	graphic_category = models.CharField(max_length=100)
	category_icon = models.CharField(max_length=100)
	upload_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.graphic.url
class Picture(models.Model):
	picture_name = models.CharField(max_length=100)
	picture = models.ImageField(storage = fs, blank=True)
	picture_url = models.URLField(max_length=100, blank=True)
	picture_no = models.IntegerField(unique=True, blank=True)
	upload_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.picture.url


class CarouselCover(models.Model):
	alt = models.CharField(max_length=10)
	cover = models.ImageField(upload_to ='backgrounds')
	upload_date = models.DateTimeField(auto_now=True)
	slide = models.IntegerField()

	def __str__(self):
		return self.cover.url

class BlogQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
	def __str__(self):
		return self.blog_title + '-' + self.blog_content + '-' + self.blog_header.url
 
class Blog(models.Model):
	blog_title = models.CharField(max_length=100)
	blog_header = models.ImageField(storage=fs)
	blog_content = RichTextField()
	tags = ArrayField(models.CharField(max_length=200), blank=True)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	objects = BlogQuerySet.as_manager()
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
	def get_absolute_url(self):
            return reverse('web:blog-detail', kwargs={'pk':self.pk})
class Story(models.Model):
	story_title = models.CharField(max_length=100)
	story = models.TextField()
	written = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.story