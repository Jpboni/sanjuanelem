from django.urls import path
from django.urls import reverse
from . import views

urlpatterns = [
	#path('<course_id>/modules/pages/newpage', views.NewPageModule, name='new-page'),
    
 	
    path('<int:code>/studentmodules/<module_id>/studentpages/<page_id>/', views.PageDetail_student, name='page-detail-student'),  
    path('<int:code>/facultymodules/<module_id>/facultypages/<page_id>/', views.PageDetail, name='page-detail'),
   
   
	#path('modules/pages/<int:code>/<page_id>', views.PageDetail, name='page-detail'),
	#path('<course_id>/modules/<module_id>/pages/<page_id>', views.PageDetail, name='page-detail'),
	#path('<course_id>/modules/<module_id>/pages/<page_id>/done', views.MarkPageAsDone, name='mark-page-as-done'),
	#path('<course_id>/modules/<module_id>/pages/newpage', NewPageModule, name='new-page'),
	#path('<course_id>/modules/<module_id>/pages/<page_id>/done', MarkPageAsDone, name='mark-page-as-done'),
]