from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    temp_num_books_word = Book.objects.all()
    num_books_word = 0
    for book in temp_num_books_word:
        if book.str().lower().__contains__('narnia'):
            num_books_word += 1
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_word':num_books_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)