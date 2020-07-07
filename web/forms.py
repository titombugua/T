from django.forms import ModelForm, Textarea
from django import forms
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
		





    


