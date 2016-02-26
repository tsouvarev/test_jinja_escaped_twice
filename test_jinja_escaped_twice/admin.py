from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from django.contrib import admin

from .models import Book, BOOK_STATUS


class JinjaListFilter(admin.FieldListFilter):
    template = 'admin/filter.jinja2'

    def expected_parameters(self):
        return dict(BOOK_STATUS).values()

    def choices(self, cl):
        return BOOK_STATUS


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = [('status', JinjaListFilter)]
