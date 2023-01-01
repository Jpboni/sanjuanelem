from . import views
from django.urls import path

urlpatterns = [
  path('School Calendar/', views.PostList.as_view(), name="PostList"),
  path('<slug:slug>/', views.PostList.as_view(), name="post_detail"),
  
]
