from django.urls import path

from book.views import BookListCreateView, BookDetailUpdateDestroy

urlpatterns = [
    path("book_list/", BookListCreateView.as_view(), name="book_list"),
    path("book/<uuid:id>/", BookDetailUpdateDestroy.as_view(), name="book_detail"),
]