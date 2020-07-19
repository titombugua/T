from django.contrib import admin
from .models import *
# from django_markdown.admin import MarkdownModelAdmin
# from django_markdown.widgets import AdminMarkdownWidget



# Register your models here.
class CarouselCaptionAdmin(admin.ModelAdmin):
	list_display = ('caption', 'caption_no', 'publish_date')		

class PortfolioGraphicAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'site_url', 'graphic', 'graphic_no', 'graphic_category', 'category_icon', 'upload_date')	

class CarouselCoverAdmin(admin.ModelAdmin):
	list_display = ('alt', 'cover', 'upload_date', 'slide')
	
class ResumeAdmin(admin.ModelAdmin):
	list_display = ('skill_icon', 'skill', 'skill_desc', 'experienced')

class BlogAdmin(admin.ModelAdmin):
	list_display = ('blog_title', 'blog_content','created')
	prepopulated_fields = {'slug': ('blog_title',)}
class PictureAdmin(admin.ModelAdmin):
	list_display = ('picture_name', 'picture')		

class TestMAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc', 'created')


admin.site.register(CarouselCaption, CarouselCaptionAdmin)
admin.site.register(About)
admin.site.register(Picture, PictureAdmin)

admin.site.register(Resume, ResumeAdmin)
admin.site.register(PortfolioGraphic, PortfolioGraphicAdmin)
admin.site.register(CarouselCover, CarouselCoverAdmin)
admin.site.register(Blog, BlogAdmin)

# Register your models here.

