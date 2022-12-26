from django.urls import path
from . import views



urlpatterns = [
    path('form/', views.form),
    path('form/calc', views.calc),
    path('formCert/', views.formCert),
    path('formCert/returnCert', views.returnCert),
    path('printCert', views.printCert)
    #path('printCert', views.printCert)

] 

