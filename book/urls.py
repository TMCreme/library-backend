from django.urls import path

from book.views import BookListCreateView

urlpatterns = [
    path("book_list/", BookListCreateView.as_view(), name="book_list"),
]