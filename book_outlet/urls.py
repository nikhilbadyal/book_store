from django.urls import path

from book_outlet import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_details, name="book-details"),
]
