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
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)




    


