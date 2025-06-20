from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        (0, 'Guest'),
        (1, 'Librarian'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ('email', 'role', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_role(self):
        role = self.cleaned_data.get('role')
        return int(role)
