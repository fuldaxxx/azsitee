from django.contrib import admin
from mptt.admin import MPTTModelAdmin




from azsite.src.wall.models import Comment


@admin.register(Comment)
class PostAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ("user", "created_date", "moderation", "published", "id", 'view_count')

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Коментарии к статьям"""
    list_display = ("user", "post", "create_date", "update_date", "published", "id")
   # actions = ['unpublish', 'publish']
    mptt_level_indent = 15
