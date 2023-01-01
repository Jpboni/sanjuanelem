from django.shortcuts import render, redirect, get_object_or_404
from main.views import is_faculty_authorised, is_student_authorised
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from main.models import  Course, Faculty ,Student
from page.models import Page, PostFileContent
from main.models import Course
from module.models import Module
from django.contrib import messages
from page.forms import NewPageForm

# Create your views here.


def addPage(request, code,module_id):
    if is_faculty_authorised(request, code):
        if request.method == 'POST':
            form = NewPageForm(request.POST)
            form.instance.module = Module.objects.get(id=module_id)
            if form.is_valid():
                form.save()
                messages.success(request, 'Module added successfully.')
                return redirect('/faculty/' + str(code))
        else:
            form = NewPageForm()
        return render(request, 'newmodule.html', {'course': Course.objects.get(code=code), 'faculty': Faculty.objects.get(faculty_id=request.session['faculty_id']), 'form': form})
    else:
        return redirect('std_login')



    

def PageDetail(request, module_id, page_id,code):
    try:
        course = Course.objects.get(code=code)
        if request.session.get('faculty_id'):
            try:
                page = get_object_or_404(Page, id=page_id)
                
            except:
                page = None

            context = {
                'course':course,
                'page': page,
                #'completed': completed,
                'faculty': Faculty.objects.get(faculty_id=request.session['faculty_id']),
                
                'module_id': module_id,
            }
	
            return render(request, 'page.html', context)
        
        else:
            
            return redirect('std_login')
    except:
        return render(request, 'error.html')
    
    
def PageDetail_student(request, module_id, page_id,code):
    try:
        course = Course.objects.get(code=code)
        if is_student_authorised(request, code):
            try:
                page = get_object_or_404(Page, id=page_id)
                
            except:
                page = None

            context = {
                'course':course,
                'page': page,
                #'completed': completed,
                'student': Student.objects.get(student_id=request.session['student_id']),
                'module_id': module_id,
            }
	
            return render(request, 'page_student.html', context)
        
        else:            
            return redirect('std_login')
    except:
        return render(request, 'error.html')
    









