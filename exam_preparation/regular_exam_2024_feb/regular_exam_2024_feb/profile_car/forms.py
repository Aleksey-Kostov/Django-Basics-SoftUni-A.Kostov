from django import forms
from .models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 21:
            raise forms.ValidationError('You must be at least 21 years old.')
        return age
