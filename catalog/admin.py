from django.contrib import admin

from .models import Genre, Book, BookInstance, Author


# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)

class AuthorInline(admin.StackedInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_of_birth','date_of_death')
    fields = ('first_name','last_name',('date_of_birth','date_of_death'))

    inlines = [AuthorInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('status','due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id', 'borrower')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass