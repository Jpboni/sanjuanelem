from django.contrib import admin
from page.models import Page
from page.models import PostFileContent

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    search_fields=['title','course_code']
    list_display=['title','course_code']
    list_filter=['title','course_code']
    
admin.site.register(Page,PageAdmin)


admin.site.register(PostFileContent)