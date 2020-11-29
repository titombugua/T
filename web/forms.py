from django.forms import ModelForm, Textarea
from django import forms
from django.core.mail import send_mail, BadHeaderError
# from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField

from .models import *

class StoryForm(ModelForm):
	
	class Meta:
		model = Story
		fields = ['story_title', 'story']
		widgets = {
			'story': Textarea(attrs={'cols': 80, 'rows': 20}),
}
		

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50)
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(max_length=100)
	comment = forms.CharField(widget=forms.Textarea)




    


