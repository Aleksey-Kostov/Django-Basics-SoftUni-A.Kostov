from django import forms
from .models import Car


class CarsCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }
        widgets = {
            'image_url': forms.URLInput(attrs={
                'placeholder': 'https://...',
            }),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 1.0:
            raise forms.ValidationError("Price must be at least 1.0.")
        return price
