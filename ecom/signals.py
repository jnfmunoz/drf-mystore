from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

from .models import Order

@receiver(valid_ipn_received)
def valid_ipn_received(sender, **kwargs):
    print("Valid IPN received")
    ipn = sender
    if ipn.payment_status == 'Completed':
        Order.objects.create()

@receiver(invalid_ipn_received)
def invalid_ipn_received(sender, **kwargs):
    print("Invalid IPN received")
    ipn = sender
    if ipn.payment_status == 'Completed':
        Order.objects.create()
