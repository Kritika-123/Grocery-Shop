from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_order_confirmation_emails(order):
    """Send order confirmation emails to both customer and admin."""
    
    # Customer Email
    customer_subject = f'Order Confirmation - Order #{order.id}'
    customer_html_message = render_to_string('cart/email/customer_order_confirmation.html', {
        'order': order,
        'delivery_details': order.delivery_details,
    })
    customer_plain_message = strip_tags(customer_html_message)
    
    send_mail(
        subject=customer_subject,
        message=customer_plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.delivery_details.email],
        html_message=customer_html_message,
    )
    
    # Admin Email
    admin_subject = f'New Order Received - Order #{order.id}'
    admin_html_message = render_to_string('cart/email/admin_order_notification.html', {
        'order': order,
        'delivery_details': order.delivery_details,
    })
    admin_plain_message = strip_tags(admin_html_message)
    
    send_mail(
        subject=admin_subject,
        message=admin_plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        html_message=admin_html_message,
    ) 