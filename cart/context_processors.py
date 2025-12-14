from .models import Cart

def cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.items.count()
        return {'cart_count': cart_count}
    return {'cart_count': 0} 