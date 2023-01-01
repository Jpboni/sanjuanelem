from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register your models here.
from .models import Student, Faculty, Course, Department, Assignment, Announcement, Material


#student

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('student_id',)
        fields=('student_id','name','email','password', 'role', 'course','department')

class Studentadmin (ImportExportModelAdmin):
    search_fields=['student_id','name','email']
    list_display=['student_id','name','email','department']
    list_filter=['student_id','name','email','department']
    resource_class = StudentResource

admin.site.register(Student,Studentadmin)


#faculty

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('faculty_id',)
        fields=('faculty_id','name','email','password', 'department','role')

class Facultyadmin (ImportExportModelAdmin):
    search_fields=['faculty_id','name','email']
    list_display=['faculty_id','name','email','department','department_id','photo']
    list_filter=['faculty_id','name','email','department','department_id']
    resource_class = FacultyResource

admin.site.register(Faculty,Facultyadmin)



#course

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo','studentKey','facultyKey')
        import_id_fields = ('code',)
        fields=('code','name', 'department','faculty') 

class Courseadmin (ImportExportModelAdmin):
    search_fields=['name']
    list_display=['code','name','department']
    list_filter=['code','name','department']
    resource_class = CourseResource


admin.site.register(Course,Courseadmin)

#department
class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('department_id',)
        fields=('department_id','name','description')

class Departmentadmin (ImportExportModelAdmin):
    search_fields=['department_id','name','description']
    list_display=['department_id','name','description']
    list_filter=['department_id','name','description']
    resource_class = DepartmentResource

admin.site.register(Department,Departmentadmin)

#assign

@admin.action(description='Change to draft')
def make_draft(AssignmentAdmin, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(AssignmentAdmin, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(AssignmentAdmin, request, queryset):
    queryset.update(status='2')



class AssignmentAdmin(admin.ModelAdmin):
    search_fields=['title','datetime','description','deadline']
    list_display=['title','deadline','datetime','description','status']
    list_filter=['title','deadline','datetime','description','status']
    actions = [make_draft,make_published,make_archived]

admin.site.register(Assignment,AssignmentAdmin)


#announce

@admin.action(description='Change to draft')
def make_draft(AnnouncementAdmin, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(AnnouncementAdmin, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(AnnouncementAdmin, request, queryset):
    queryset.update(status='2')
    
class AnnouncementAdmin(admin.ModelAdmin):
    search_fields=['datetime','description','status']
    list_display=['datetime','description','status']
    list_filter=['datetime','description','status']
    actions = [make_draft,make_published,make_archived]
   

admin.site.register(Announcement,AnnouncementAdmin)



#mats

@admin.action(description='Change to draft')
def make_draft(MaterialAdmin, request, queryset):
    queryset.update(status='0')

@admin.action(description='Change to published')
def make_published(MaterialAdmin, request, queryset):
    queryset.update(status='1')

@admin.action(description='Change to archived')
def make_archived(MaterialAdmin, request, queryset):
    queryset.update(status='2')
    
class MaterialAdmin(admin.ModelAdmin):
    search_fields=['datetime','file','status']
    list_display=['course_code','datetime','file','status']
    list_filter=['course_code','datetime','file','status']
    actions = [make_draft,make_published,make_archived]


admin.site.register(Material,MaterialAdmin)
