from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.list import ListView
from . import views
from web import views
from .models import Blog, About, Resume

app_name = 'web'

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
    url(r'^form/$', views.add_story, name='add-story'),
   	url(r'^about-me/$', ListView.as_view(queryset=Resume.objects.all()), name='about-me'),
   		url(r'^contact/$', views.contact, name='contact'),
   		   		url(r'^resume/$', views.resume, name='resume'),



	url(r'^blog/$', ListView.as_view(queryset=Blog.objects.published().order_by("-created")), name='blog'),
	url(r'^blog/add/$', views.BlogCreate.as_view(), name='blog-add'),
	url(r'blog/(?P<pk>[0-9]+)/$', views.BlogUpdate.as_view(), name='blog-update'),
	url(r'blog/(?P<pk>[0-9]+)/delete/$', views.BlogDelete.as_view(), name='blog-delete'),
	url(r'^blog/detail/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
]

