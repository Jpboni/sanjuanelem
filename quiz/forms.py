from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Quiz, Question


class QuizForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.fields['publish_status'].label = "View Score Immediately "
        

  class Meta:
         model = Quiz
         fields = ['title', 'start','end','publish_status','status']

         widgets = {

             'title': forms.TextInput(attrs={'class': 'form-control ', 'id': 'title', 'name': 'title', 'placeholder': 'Quiz Title'}),
             'start': forms.DateTimeInput(attrs={'class': 'form-control ', 'id': 'deadline', 'name': 'deadline', 'type': 'datetime-local'}),
             'end': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'end', 'name': 'deadline', 'type': 'datetime-local'}),
             'publish_status': forms.CheckboxInput(attrs={})
        }

class QuestionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        

  class Meta:
         model = Question
         CHOICES= (('A','A'),('B','B'),('C','C'),('D','D'))
         fields = ['question', 'option1','option2','option3','option4','answer','marks','explanation']
         field = forms.ChoiceField(choices=CHOICES)
         

         widgets = {

             'question': forms.TextInput(attrs={'class': 'form-control ', 'id': 'question', 'name': 'question', 'placeholder': 'Question'}),
             'option1': forms.TextInput(attrs={'class': 'form-control ', 'id': 'option1', 'name': 'option1'}),
             'option2': forms.TextInput(attrs={'class': 'form-control', 'id': 'option2', 'name': 'option2', }),
             'option3': forms.TextInput(attrs={'class': 'form-control', 'id': 'option3', 'name': 'option3', }),
             'option4': forms.TextInput(attrs={'class': 'form-control', 'id': 'option4', 'name': 'option4', }),
             'answer' : forms.Select(attrs={'class': 'form-control', 'id': 'answer',}),
             'marks': forms.NumberInput(attrs={'class': 'form-control' }),
             'explanation': forms.TextInput(attrs={'class': 'form-control', 'id': 'explanation', 'name': 'explanation',}),
             

        }






