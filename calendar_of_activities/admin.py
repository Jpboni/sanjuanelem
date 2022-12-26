from django.contrib import admin

# Register your models here.
from .models import Post


@admin.action(description='Change to draft')
def make_draft(PostAdmin, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(PostAdmin, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(PostAdmin, request, queryset):
    queryset.update(status='2')
    

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'status', 'created_on','date_of_event','status')
  list_filter = ('status',)
  search_fields = ['title','date_of_event','status']
  actions = [make_draft,make_published,make_archived]
  
admin.site.register(Post, PostAdmin)