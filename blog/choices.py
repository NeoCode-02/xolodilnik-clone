from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BlogPostStatus(TextChoices):
    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")
