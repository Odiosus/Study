from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

def nullfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)

nullfy_rating.short_description = 'Обнулить рейтинг'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create', 'category_list')
    list_filter = ('author', 'type', 'category')
    search_fields = ('title', 'author__authorUser__username')
    actions = [nullfy_rating]


class CategoryAdmin(TranslationAdmin):
    model = Category

class PostlAdmin(TranslationAdmin):
    model = Post


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscriptions)
