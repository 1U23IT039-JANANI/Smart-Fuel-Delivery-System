from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Order
from .forms import UserRegisterForm

# -------------------------------
# User Registration
# -------------------------------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# -------------------------------
# Dashboard - Shows user orders
# -------------------------------
@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'orders': orders})

# -------------------------------
# Book Fuel Order
# -------------------------------
@login_required
def book_order(request):
    if request.method == 'POST':
        # Get values from POST
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Create order
        Order.objects.create(
            user=request.user,
            fuel_type=request.POST.get('fuel_type'),
            liters=request.POST.get('liters'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            latitude=float(latitude) if latitude else None,
            longitude=float(longitude) if longitude else None
        )

        # Add confirmation message
        messages.success(request, 'Fuel order booked successfully!')

        return redirect('dashboard')

    return render(request, 'book_order.html')

# -------------------------------
# Track Specific Order
# -------------------------------
@login_required
def track_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'track_order.html', {'order': order})