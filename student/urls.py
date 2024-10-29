from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path("list/", student_list, name="list"),
    path("detail/<int:pk>", student_detail, name="detail"),
]
