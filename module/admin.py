from django.contrib import admin
from module.models import Module

# Register your models here.


@admin.action(description='Change to draft')
def make_draft(ModuleAdmin, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(ModuleAdmin, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(ModuleAdmin, request, queryset):
    queryset.update(status='2')
    
class ModuleAdmin(admin.ModelAdmin):
    search_fields=['title']
    list_display=['title','course_code','status']
    list_filter=['course_code','status']
    actions = [make_draft,make_published,make_archived]
   

admin.site.register(Module,ModuleAdmin)