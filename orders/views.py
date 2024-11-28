from django.shortcuts import render
from orders.services import add_order

def orders(request):
    context = {
        'title': 'Orders',
    }
    return render(request, 'orders.html', context)

def add_order_view(request):
    add_order()