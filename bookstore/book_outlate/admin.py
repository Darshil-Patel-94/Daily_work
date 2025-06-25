from django.contrib import admin
from .models import Book , Author , Adress

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}
  list_filter = ("author","ratting")
  list_display = ("title", "author",)
  
class autoradmin(admin.ModelAdmin):
  list_display = ("first_name",)

admin.site.register(Book , BookAdmin)
admin.site.register(Author)
admin.site.register(Adress)

