from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.http import HttpResponseRedirect


def homepage(request):
	# Home
	cover_img = CarouselCover.objects.get(slide=0)
	cover_img_1 = CarouselCover.objects.get(slide=1)
	cover_img_2	 = CarouselCover.objects.get(slide=2)
	# caption_item = CarouselCaption.objects.get(caption_no=1)
	# caption_item_1 = CarouselCaption.objects.get(caption_no=2)
	# caption_item_2 = CarouselCaption.objects.get(caption_no=3)
	# caption_item_3 = CarouselCaption.objects.get(caption_no=4)
	#About
	bio_desc = About.objects.order_by('publish_date')[0]
	#Resume
	skill_list = Resume.objects.all()
	# # Portfolio
	graphic_item = PortfolioGraphic.objects.get(graphic_no=0)
	graphic_item_1 = PortfolioGraphic.objects.get(graphic_no=1)
	graphic_item_2 = PortfolioGraphic.objects.get(graphic_no=2)
	pictures = Picture.objects.all()
	# # Blog-Preview
	# queryset = Blog.objects.published()[:2]
	
	context = {
		'cover_img': cover_img,
		'cover_img_1': cover_img_1,
		'cover_img_2': cover_img_2,
		# 'caption_item': caption_item,
		# 'caption_item_1': caption_item_1,
		# 'caption_item_2': caption_item_2,
		# 'caption_item_3': caption_item_3,
		'bio_desc': bio_desc,
		'skill_list': skill_list,
		'graphic_item': graphic_item,
		'graphic_item_1': graphic_item_1,
		'graphic_item_2': graphic_item_2,
		'pictures':pictures,
		# 'queryset':queryset,
		}
	return render(request, 'layout.html', context)
def resume(request):
	return render(request, 'resume_list.html')
def contact(request):
	return render(request, 'contact_list.html')


class BlogCreate(CreateView):
	model = Blog
	fields = ['blog_title','blog_content']
class BlogUpdate(UpdateView):
	model = Blog
	fields = ['blog_title', 'blog_content', 'publish_date']
	template_name_suffix = '_update_form'

class BlogDelete(DeleteView):
	model = Blog
	# fields = ['blog_title', 'Blog_content', 'publish_date']
	success_url = reverse_lazy('web:homepage')
class BlogDetailView(DetailView):
	queryset = Blog.objects.all()
	def get_object(self):
		object = super(BlogDetailView, self).get_object()
		return object
# class ContactView(FormView):
# 	template_name = 'blogg.html'
# 	form_class = BlogForm
# 	success_url = '/blog/'
def add_story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/')
	else:
		form = StoryForm()
	return render(request, 'bf.html', {'form': form})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['julesmbugua@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_list.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
