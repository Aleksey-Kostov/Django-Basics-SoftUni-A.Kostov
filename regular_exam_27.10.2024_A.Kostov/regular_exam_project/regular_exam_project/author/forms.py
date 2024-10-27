from django import forms
from django.core.exceptions import ValidationError

from regular_exam_project.author.models import Author


class AuthorCreationForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}, render_value=False),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits',
        }

    def clean_passcode(self):
        passcode = self.cleaned_data.get('passcode')
        if not passcode.isdigit() or len(passcode) != 6:
            raise ValidationError("Your passcode must be exactly 6 digits!")
        return passcode

    def clean_pets_number(self):
        pets_number = self.cleaned_data.get('pets_number')
        if pets_number < 0:
            raise ValidationError("Number of pets cannot be negative!")
        return pets_number
