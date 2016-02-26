from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from django.db import models


BOOK_STATUS = (
    (0, 'Unpublished'),
    (1, 'Published'),
)


class Book(models.Model):
    name = models.CharField('name', max_length=255)
    status = models.IntegerField(choices=BOOK_STATUS)
