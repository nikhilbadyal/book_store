from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from .models import Book


# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    total_books = books.all().count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_books": total_books,
        "average_rating": average_rating
    })


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html", {
        "book": book
    })
