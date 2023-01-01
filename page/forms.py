from django import forms
from froala_editor.widgets import FroalaEditor
from page.models import Page

class NewPageForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	content = forms.CharField(widget=FroalaEditor(attrs={'class': 'validate'}), required=True)
	files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

	class Meta:
		model = Page
		#fields = '__all__'
		fields = ('title', 'content', 'files')