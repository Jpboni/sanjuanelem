from django.contrib import admin
from . models import Quiz, Question, StudentAnswer
# Register your models here.

class QuizAdmin (admin.ModelAdmin):
    search_fields=['title','description','start','end']
    list_display=['title','course','description','start','end','status']
    list_filter=['title','course','description','start','end','status','course']


admin.site.register(Quiz,QuizAdmin)


class QuestionAdmin (admin.ModelAdmin):
    search_fields=['marks','answer','explanation']
    list_display=['quiz','question','marks','answer','explanation']
    list_filter=['quiz','question','marks','answer','explanation']

admin.site.register(Question,QuestionAdmin)


