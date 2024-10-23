from django import forms

from regular_exam_2024_feb.car.models import Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
