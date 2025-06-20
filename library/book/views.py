from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from .models import Book
from .forms import BookForm 
from author.models import Author
from order.models import Order
from authentication.models import CustomUser

User = get_user_model()

def is_librarian(user):
    return user.is_authenticated and user.role == 1

@login_required
def books_list(request):
    author_id = request.GET.get('author')
    title = request.GET.get('title')

    books = Book.objects.all()
    if author_id:
        books = books.filter(authors__id=author_id)
    if title:
        books = books.filter(name__icontains=title)

    authors = Author.objects.all()
    return render(request, 'book/books.html', {'books': books, 'authors': authors})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

@login_required
@user_passes_test(is_librarian)
def books_for_user(request, user_id):
    users = CustomUser.objects.all().prefetch_related(
        Prefetch(
            'order_set',
            queryset=Order.objects.filter(end_at__isnull=True).select_related('book')
        )
    )
    return render(request, 'book/books_for_user.html', {'users': users})

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

@login_required
@user_passes_test(is_librarian)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})
