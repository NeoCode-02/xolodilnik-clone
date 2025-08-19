from django.urls import path
from .views import *

urlpatterns = [
    path("posts", BlogPostListView.as_view(), name="blog-list"),
    path("posts/<int:pk>", BlogPostDetailView.as_view(), name="blog-detail"),
    path("posts/create", BlogPostCreateView.as_view(), name="blog-create"),
    path("posts/update/<int:pk>", BlogPostUpdateView.as_view(), name="blog-update"),
    path("posts/delete/<int:pk>", BlogPostDeleteView.as_view(), name="blog-delete"),
    path("categories", BlogCategoryListView.as_view(), name="blog-category-list"),
    path("categories/<int:pk>", BlogCategoryDetailView.as_view(), name="blog-category-detail"),
    path("categories/create", BlogCategoryCreateView.as_view(), name="blog-category-create"),
    path("categories/update/<int:pk>", BlogCategoryUpdateView.as_view(), name="blog-category-update"),
    path("categories/delete/<int:pk>", BlogCategoryDeleteView.as_view(), name="blog-category-delete"),
    path("tags", TagListView.as_view(), name="blog-tag-list"),
    path("tags/<int:pk>", TagDetailView.as_view(), name="blog-tag-detail"),
    path("tags/create", TagCreateView.as_view(), name="blog-tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="blog-tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="blog-tag-delete"),
]