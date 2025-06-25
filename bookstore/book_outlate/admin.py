from django.contrib import admin
from .models import Book , Author , Adress , Country

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}
  list_filter = ("author","ratting")
  list_display = ("title", "author",)
  
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "book_titles")

admin.site.register(Book , BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Adress)
admin.site.register(Country)

