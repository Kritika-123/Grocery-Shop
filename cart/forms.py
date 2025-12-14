from django import forms
from .models import DeliveryDetails

class DeliveryDetailsForm(forms.ModelForm):
    class Meta:
        model = DeliveryDetails
        fields = ['full_name', 'phone_number', 'email', 'address_line1', 'address_line2', 
                 'city', 'state', 'postal_code', 'additional_instructions']
        widgets = {
            'additional_instructions': forms.Textarea(attrs={'rows': 3}),
        } 