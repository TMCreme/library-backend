from django.shortcuts import render
from rest_framework import generics

from book.serializer import BookSerializer
from book.models import Book

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    