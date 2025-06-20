from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from order.models import Order
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def home_view(request):
    return render(request, 'authentication/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid credentials"
            return render(request, 'authentication/login.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('authentication:login')

def is_librarian(user):
    return user.is_authenticated and user.role == 1

@login_required
@user_passes_test(is_librarian)
def users_list(request):
    users = CustomUser.objects.all()
    return render(request, 'authentication/users.html', {'users': users})

@login_required
@user_passes_test(is_librarian)
def user_detail(request, user_id):
    user_obj = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'authentication/user_detail.html', {'user_obj': user_obj})

@login_required
@user_passes_test(is_librarian)
def books_for_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    active_orders = Order.objects.filter(user=user, end_at__isnull=True).select_related('book')
    context = {
        'user': user,
        'orders': active_orders,
    }
    return render(request, 'book/books_for_user.html', context)
