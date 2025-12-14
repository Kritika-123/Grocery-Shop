from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    """Display user profile"""
    from cart.models import Order
    from django.db.models import Sum

    # Calculate total spend from completed orders
    total_spent = Order.objects.filter(
        user=request.user,
        status__in=['delivered', 'shipped']
    ).aggregate(total=Sum('total_amount'))['total'] or 0

    # Get recent orders
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]

    return render(request, 'accounts/profile.html', {
        'total_spent': total_spent,
        'recent_orders': recent_orders,
    })


@login_required
def edit_profile(request):
    """Edit user profile information"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def my_orders(request):
    """Display user's order history"""
    from cart.models import Order

    # Get all orders for the user
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/my_orders.html', {'orders': orders})


@login_required
def settings(request):
    """Display user settings page"""
    return render(request, 'accounts/settings.html')