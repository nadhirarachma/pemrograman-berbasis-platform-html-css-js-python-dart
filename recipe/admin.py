from django.contrib import admin
# from .models import Comment
# # Register your models here.


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email',  'publish', 'status')
#     list_filter = ('status', 'publish')
#     search_fields = ('name', 'email', 'content')
#     actions = ['approve_comments']
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)