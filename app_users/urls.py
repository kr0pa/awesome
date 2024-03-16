from django.urls import path
from . import views

app_name='app_users'
urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.profile_delete, name='profile_delete'),
    path('onboarding/', views.profile_edit, name='profile_onboarding'),
    path('<username>/', views.profile_view, name='userprofile_view'),
]