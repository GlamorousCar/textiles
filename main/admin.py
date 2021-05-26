
# Register your models here.
from django.contrib import admin
from .models import Category, Product, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created_at', 'updated_at', 'category','quantity','availability')
    list_display_links = ('title', 'category')
    search_fields = ('title', 'price')
    inlines = [GalleryInline, ]


admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
