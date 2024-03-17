from django.contrib import admin
from django.urls import path
from app_posts.views import home_view, index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('index/', index_view),
]
