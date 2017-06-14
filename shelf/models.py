from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-last_name', )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_at = models.DateField()
    isbn = models.CharField(max_length=16, blank=False)

    class Meta:
        ordering = ('-published_at', )

    def __str__(self):
        return self.title
