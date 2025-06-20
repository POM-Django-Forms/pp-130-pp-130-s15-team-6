from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order
from .forms import OrderForm
from book.models import Book
from authentication.models import CustomUser

@staff_member_required
def orders_list(request):
    orders = Order.get_all()
    return render(request, 'order/orders_list.html', {'orders': orders})

@staff_member_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Можна виставити дату початку зараз
            order.start_at = timezone.now()
            order.save()
            return redirect('orders-list')
    else:
        form = OrderForm()
    return render(request, 'order/order_form.html', {'form': form})

@staff_member_required
def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders-list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/order_form.html', {'form': form})

@staff_member_required
def order_delete(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('orders-list')
