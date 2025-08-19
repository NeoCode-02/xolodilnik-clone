from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.choices import BlogPostStatus
from common.models import BaseModel

User = get_user_model()


class BlogPost(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date="published_at")
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=BlogPostStatus.choices, default=BlogPostStatus.DRAFT
    )
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    category = models.ForeignKey(
        "blog.BlogCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )
    tags = models.ManyToManyField("blog.Tag", blank=True, related_name="posts")

    class Meta:
        ordering = ["-published_at"]
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")

    def __str__(self):
        return self.title


class BlogCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Comment(BaseModel):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
