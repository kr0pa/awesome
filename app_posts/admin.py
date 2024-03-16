from django.contrib import admin
from .models import Post, Tag, Comment

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)