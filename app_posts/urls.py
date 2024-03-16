from django.urls import path
from . import views

app_name = 'app_posts'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('post/<uuid:pk>/', views.post_page_view, name="post_view"),
    path('post/<slug:tag>/', views.home_view, name="category_view"),
    path('create/', views.created_view, name="post_create"),
    path('delete/<uuid:pk>/', views.delete_view, name="post_delete"),
    path('edit/<uuid:pk>/', views.edit_view, name="post_edit"),
]