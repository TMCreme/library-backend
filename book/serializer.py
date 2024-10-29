from rest_framework import serializers

from .models import Book

# def validate_date(data):
#         """
#         Validate published date to be before today
#         """
#         if data > date.today():
#             raise serializers.ValidationError("Published date cannot be after today")
#         return data


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "isbn", "date_published", "publisher"]
