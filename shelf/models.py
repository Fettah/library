from django.db import models
from django.db.models.signals import m2m_changed
import datetime
from django.dispatch import receiver

class OldBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_at__lte=datetime.datetime(2017, 1, 1, 0, 0))


class NewBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_at__gte=datetime.datetime(2017, 1, 1, 0, 0))


class AllBooksManager(models.Manager):
    def queryset(self):
        return super().get_queryset().all()

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_nice = models.BooleanField(default=False, verbose_name='is nice ?')

    class Meta:
        ordering = ('-last_name', )

    def __str__(self):
        return self.first_name + " " + self.last_name

    def nice(self):
        if self.is_nice:
            return 'Nice One'
        else:
            return 'NOT nice one'

    nice.short_description = "Is he nice ?"

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_at = models.DateField()
    isbn = models.CharField(max_length=16, blank=False)

    def was_published_recently(self):
        return True
    was_published_recently.short_description = "Is he/she Nice ?"
    all_books = AllBooksManager()
    objects = models.Manager()
    old_books = OldBooksManager()
    # new_books = NewBooksManager()

    class Meta:
        ordering = ('-published_at', )

    def __str__(self):
        return self.title

    def pre_init(self):
        print("pre_init is triggered")


class Tag(models.Model):
    books = models.ManyToManyField(Book, related_name='books')
    name = models.CharField(max_length=255)

@receiver(m2m_changed, sender=Tag.books.through)
def book_changed(sender, **kwargs):
    import pdb;pdb.set_trace()
    print(sender)
    print(kwargs)

    print("book updated has changed")

