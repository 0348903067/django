from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # Hiển thị các trường này trong danh sách sản phẩm
    search_fields = ('name', 'category')  # Thêm tính năng tìm kiếm theo tên và danh mục
    list_filter = ('category',)  # Bộ lọc theo danh mục

admin.site.register(Product, ProductAdmin)
