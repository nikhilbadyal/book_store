from django.contrib import admin

from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "author", "rating")
    list_display = ("title", "author", "rating")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
