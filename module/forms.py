from django import forms
from module.models import Module
from module.models import Module


class ModuleForm(forms.ModelForm):
		def __init__(self, *args, **kwargs):
			super(ModuleForm, self).__init__(*args, **kwargs)
			for field in self.fields.values():
				field.required = True
				self.fields['title'].label = 'Module Title'
				
				
  
		class Meta:
			model = Module
			fields = ['title','pages','status']
			widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-1', 'id': 'title', 'name': 'title', 'placeholder': 'Title'}),
            'pages': forms.SelectMultiple(attrs={'class': 'form-control mt-1', 'id': 'file', 'name': 'file'}),
        
        }
