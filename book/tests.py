from django.test import TestCase
from django.urls import reverse

from book.models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Test Title",
            author="Ama Test",
            isbn="123123123",
            date_published="2000-12-12",
            publisher="Pub Test"
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "Ama Test")
        self.assertEqual(self.book.date_published, "2000-12-12")
        self.assertEqual(self.book.publisher, "Pub Test")