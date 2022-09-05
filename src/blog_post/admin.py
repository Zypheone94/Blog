from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'isPublished',
        'date',
        'get_categories'
    )

    list_per_page = 5

    autocomplete_fields = (
        'author',
    )

    list_editable = (
        'isPublished',
    )

    search_fields = (
        'title',
    )

    list_filter = (
        'author',
    )

    empty_value_display = 'Non spécifié'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
