from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'zuo', 'content']


admin.site.register(Book, BookAdmin)
