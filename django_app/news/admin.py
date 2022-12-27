from django.contrib import admin

from .models import *

# Дополнительные поля в админ панели у блоков
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'author_id', 'price', 'amount') # поля
     list_display_links = ('title', 'author_id') # поля-ссылки для редактированния
     search_fields = ('title', 'author') # поиск
     list_filter = ('author_id', 'price', 'amount')

class AuthorAdmin(admin.ModelAdmin):
     list_display =('name_author',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(City)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Step)