from django.contrib import admin
from .models import Book, Librarian, Category

admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Category)
