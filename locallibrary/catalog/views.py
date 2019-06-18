from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Books and Genres with Chicken in them
    num_chicken_books = Book.objects.filter(title__contains='chicken').count()

    # Genres with Self in them
    num_self_genres = Genre.objects.filter(name__contains='self').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_chicken_books': num_chicken_books,
        'num_self_genres': num_self_genres,
    }

    # Render the HTML template index.html with the data
    # in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # # specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.ListView):
    model = Author


