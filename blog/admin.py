from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import BlogCategory, BlogPost, Comment, Tag


@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    list_display = ("id", "title", "status", "published_at")
    list_display_links = ("id", "title")
    list_filter = ("status", "published_at")
    search_fields = ("title", "slug", "category", "tags")
    date_hierarchy = "published_at"
    ordering = ["-published_at"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "user",
                    "slug",
                    "image",
                    "status",
                    "category",
                    "tags",
                    "is_featured",
                    "published_at",
                )
            },
        ),
         (
            _("Uzbek"),
            {
                "fields": (
                    "title_uz",
                    "content_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "title_en",
                    "content_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "content_ru",
                )
            },
        ),
    )

    readonly_fields = ("slug", "published_at")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "user", "category", "tags", "published_at"]

@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "is_active")
    list_display_links = ("id", "name")
    list_filter = ("is_active",)
    search_fields = ("name",)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name", "is_active"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "is_active",
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                )
            },
        ),
    )

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "name"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                   
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                )
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                )
            },
        ),
    )   
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "is_active")
    list_display_links = ("id", "user", "post")
    list_filter = ("is_active",)
    search_fields = ("user", "post")
    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "user",
                    "post",
                    "is_active",
                )
            },
        ),
    )
