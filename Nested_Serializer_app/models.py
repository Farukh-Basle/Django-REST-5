from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)
    add = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_price = models.FloatField()
    publish_date = models.DateField()

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        related_name= 'Books_by_Author'
    )

