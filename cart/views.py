from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from products.models import Product
from .models import Cart, CartItem, Order, DeliveryDetails
from .forms import DeliveryDetailsForm
from .utils import send_order_confirmation_emails
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity += quantity
        cart_item.save()
    else:
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()
    
    messages.success(request, f'{product.name} added to your cart.')
    return redirect(request.META.get('HTTP_REFERER', reverse('cart:cart_detail')))

@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(cart=cart, product=product).delete()
    messages.success(request, f'{product.name} removed from your cart.')
    return redirect('cart:cart_detail')

@login_required
def cart_update(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f'Quantity of {product.name} updated to {quantity}.')
    else:
        cart_item.delete()
        messages.success(request, f'{product.name} removed from your cart.')
    
    return redirect('cart:cart_detail')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    if request.method == 'POST':
        form = DeliveryDetailsForm(request.POST)
        if form.is_valid():
            try:
                # Get payment method from form
                payment_method = request.POST.get('payment_method', 'cod')
                
                # Create order first
                order = Order.objects.create(
                    user=request.user,
                    total_amount=cart.total_price,
                    payment_method=payment_method
                )
                
                # Create delivery details with the order
                delivery_details = form.save(commit=False)
                delivery_details.user = request.user
                delivery_details.order = order
                delivery_details.save()
                
                # Update order with delivery details
                order.delivery_details = delivery_details
                order.save()
                
                # Add items to order
                for cart_item in cart.items.all():
                    order.items.add(cart_item.product)
                
                # Send order confirmation emails
                try:
                    send_order_confirmation_emails(order)
                    email_sent = True
                except Exception as e:
                    logger.error(f"Failed to send order confirmation emails: {str(e)}")
                    email_sent = False
                
                # Clear the cart
                cart.items.all().delete()
                cart.save()
                
                # Show success message with email status
                if email_sent:
                    messages.success(request, f'Order #{order.id} placed successfully! You will receive an email confirmation shortly.')
                else:
                    messages.success(request, f'Order #{order.id} placed successfully! However, there was an issue sending the confirmation email.')
                
                return redirect('accounts:profile')
                
            except Exception as e:
                messages.error(request, f'An error occurred while processing your order: {str(e)}')
                return redirect('cart:cart_detail')
    else:
        form = DeliveryDetailsForm()
    
    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'cart/checkout.html', context) 