import uuid
from django.db import models


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=30)
    # date_published fied has been set to VARCHAR
    date_published = models.DateField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
