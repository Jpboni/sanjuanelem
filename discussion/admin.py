from django.contrib import admin
from .models import FacultyDiscussion, StudentDiscussion
# Register your models here.

@admin.action(description='Change to Archived')
def make_draft(StudentDiscussion, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to Published')
def make_published(StudentDiscussion, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to Offensive')
def make_archived(StudentDiscussion, request, queryset):
    queryset.update(status='2')

class Studentadmin (admin.ModelAdmin):
    search_fields=['content','status']
    list_display=['sent_by','content','course','status']
    list_filter=['content','course','status']
    actions = [make_draft,make_published,make_archived]
    

admin.site.register(StudentDiscussion,Studentadmin)

@admin.action(description='Change to draft')
def make_draft(FacultyDiscussion, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(FacultyDiscussion, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(FacultyDiscussion, request, queryset):
    queryset.update(status='2')

class Facultyadmin (admin.ModelAdmin):
    search_fields=['content','status' ]
    list_display=['sent_by','content','course','status']
    list_filter=['content','course','status']
    actions = [make_draft,make_published,make_archived]
    

admin.site.register(FacultyDiscussion,Facultyadmin)


    


