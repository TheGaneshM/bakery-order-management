from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def dashboard(request):

    total_orders = Order.objects.count()

    pending_orders = Order.objects.filter(
        status='Pending'
    ).count()

    completed_orders = Order.objects.filter(
        status='Completed'
    ).count()

    context = {
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders
    }

    return render(
        request,
        'orders/dashboard.html',
        context
    )


def order_list(request):

    orders = Order.objects.all()

    return render(
        request,
        'orders/order_list.html',
        {'orders': orders}
    )


def add_order(request):

    form = OrderForm()

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('order_list')

    return render(
        request,
        'orders/add_order.html',
        {'form': form}
    )


def update_order(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('order_list')

    return render(
        request,
        'orders/add_order.html',
        {'form': form}
    )


def delete_order(request, pk):

    order = Order.objects.get(id=pk)
    order.delete()

    return redirect('order_list')