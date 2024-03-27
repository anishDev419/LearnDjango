from django.contrib import admin
from books.models import Books


# Register your models here.
@admin.register(Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

