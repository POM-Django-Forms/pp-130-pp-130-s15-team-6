from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Author
from .forms import AuthorForm 

def home_view(request):
    return render(request, 'author/home.html')

@staff_member_required
def authors_list(request):
    authors = Author.get_all()
    return render(request, 'author/authors_list.html', {'authors': authors})

@staff_member_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
    else:
        form = AuthorForm()
    return render(request, 'author/author_form.html', {'form': form})

@staff_member_required
def author_edit(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author/author_form.html', {'form': form})

@staff_member_required
def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if not hasattr(author, 'book_set') or author.book_set.count() == 0:
        author.delete_by_id(author_id)
    return redirect('authors-list')
