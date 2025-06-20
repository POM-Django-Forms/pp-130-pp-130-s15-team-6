from django import forms
from .models import Order
from book.models import Book
from authentication.models import CustomUser

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'book', 'end_at']
        widgets = {
            'end_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        return cleaned_data
