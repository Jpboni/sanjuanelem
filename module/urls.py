from django.urls import path
from django.urls import reverse
from . import views

urlpatterns = [
    #Modules
    path('CourseModules_student/<int:code>/', views.CourseModules_student, name='CourseModules_student'),
	path('CourseModules/<int:code>/', views.CourseModules, name='CourseModules'),
	path('deleteModules/<int:code>/<int:id>/', views.deleteModules, name='deleteModules'),
	path('addModules/<int:code>/', views.addModules, name='addModules'),
 	path('editModules/<int:code>/<int:id>/', views.editModules, name='editModules'),
 	path('updateModules/<int:code>/<int:id>/', views.updateModules, name='updateModules'),
  	

]