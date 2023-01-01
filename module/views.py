from django.shortcuts import render, get_object_or_404, redirect
from main.views import is_faculty_authorised, is_student_authorised
from django.http import HttpResponseForbidden
from module.forms import ModuleForm
from .models import Module, Page
from main.models import  Course, Faculty ,Student
from django.contrib import messages
#from classroom.models import Course

#from completion.models import Completion
from .models import Course
# Create your views here.



def CourseModules(request, code):
	if request.session.get('faculty_id'):
		course = Course.objects.get(code=code)
		try:
			module = Module.objects.filter(course_code=course)
			page= Page.objects.filter(course_code=course)
        
		except:
			module = None
			page = None
			   
		context = {
		'course': course,
  		'module': module,
   		'faculty': Faculty.objects.get(faculty_id=request.session['faculty_id']),
    	'page': page,

		}
		return render(request, 'modules.html', context)

	else:
		return redirect('std_login')


def CourseModules_student(request, code):
	try:
		course = Course.objects.get(code=code)
		if is_student_authorised(request, code):
			try:
				module = Module.objects.filter(status=1,course_code=course)
				page= Page.objects.filter(course_code=course)
   
			except:
				module = None
				page = None
							
			context = {
			'course': course,
			'module': module,
			'student': Student.objects.get(student_id=request.session['student_id']),
			'page': page,

			}
			return render(request, 'modules_student.html', context)
		else:
			return redirect('std_login')
	except:
			return render(request, 'error.html')

def addModules(request, code):
    if is_faculty_authorised(request, code):
        if request.method == 'POST':
            form = ModuleForm(request.POST)
            form.instance.course_code = Course.objects.get(code=code)
            if form.is_valid():
                form.save()
                messages.success(request, 'Module added successfully.')
                return redirect('/faculty/' + str(code))
        else:
            form = ModuleForm()
        return render(request, 'newmodule.html', {'course': Course.objects.get(code=code), 'faculty': Faculty.objects.get(faculty_id=request.session['faculty_id']), 'form': form})
    else:
        return redirect('std_login')
    
def deleteModules(request, code, id):
    if is_faculty_authorised(request, code):
        try:
            module = Module.objects.get(course_code=code, id=id)
            module.delete()
            messages.warning(request, 'Module deleted successfully.')
            return redirect('/faculty/' + str(code))
        except:
            return redirect('/faculty/' + str(code))
    else:
        return redirect('std_login')
    
def editModules(request, code, id):
    if is_faculty_authorised(request, code):
        module = Module.objects.get(course_code_id=code, id=id)
        form = ModuleForm(instance=module)
        context = {
            'module': module,
            'course': Course.objects.get(code=code),
            'faculty': Faculty.objects.get(faculty_id=request.session['faculty_id']),
            'form': form
        }
        return render(request, 'main/update-module.html', context)
    else:
        return redirect('std_login')

def updateModules(request, code, id):
    if is_faculty_authorised(request, code):
        try:
            module = Module.objects.get(course_code_id=code, id=id)
            form = ModuleForm(request.POST, instance=module)
            if form.is_valid():
                form.save()
                messages.info(request, 'Module updated successfully.')
                return redirect('/faculty/' + str(code))
        except:
            return redirect('/faculty/' + str(code))

    else:
        return redirect('std_login')