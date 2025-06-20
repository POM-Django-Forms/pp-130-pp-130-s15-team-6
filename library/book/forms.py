from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors', 'publication_year', 'issue_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва книги'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис книги'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Кількість'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рік публікації'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Назва книги',
            'description': 'Опис книги',
            'count': 'Кількість',
            'authors': 'Автор(и)',
            'publication_year': 'Рік видання',
            'issue_date': 'Дата видачі',
        }
