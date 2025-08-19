from django.contrib import admin

from blog.models import BlogCategory, BlogPost, Comment, Tag


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "published_at")
    list_display_links = ("id", "title")
    list_filter = ("status", "published_at")
    search_fields = ("title", "content")
    date_hierarchy = "published_at"
    ordering = ["-published_at"]


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_display_links = ("id", "name")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "is_active")
    list_display_links = ("id", "user", "post")
    list_filter = ("is_active",)
    search_fields = ("user", "post")
