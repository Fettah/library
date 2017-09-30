from django.contrib import admin
from shelf.models import Book, Author


# fields -> for the form
# fieldset -> create a formset -> choose names and list of attributes.
# eg. ('title of this book', {'fields': ['title', 'published_at']}),

# list_display -> list of attributes to display in the list page
# actions -> dropdown -> bulk update.
# list_filter
# search_fields
# list_display_links -> make elemts linkable
# self.message_users() -> flash

class BookInline(admin.StackedInline):
    model = Book
    extra = 2


class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'author', 'published_at']
    fieldsets = [
        ('Book information', {'fields': ['title', 'published_at']}),
        ('Author Data', {'fields': ['author'], 'classes': 'collapses'})
    ]

    list_filter = ('published_at', 'isbn', 'author')
    list_display = ['title', 'published_at', 'isbn', 'author']
    list_display_links = ['published_at']
    list_editable = ['isbn']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    inlines = (BookInline, )

    list_display = ('first_name', 'last_name', 'is_nice')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', )
    actions = ['make_all_nice', 'make_all_not_nice']

    def make_all_nice(self, request, queryset):
        queryset.update(is_nice=True)
        self.message_user(request, "action was successfully completed")
    make_all_nice.short_description = "Make selected as nice"

    def make_all_not_nice(self, request, queryset):
        queryset.update(is_nice=False)
    make_all_not_nice.short_description = "Make selected as Not nice"


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
