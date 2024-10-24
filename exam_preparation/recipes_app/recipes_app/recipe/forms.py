from django import forms
from .models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        labels = {
            'title': 'Title',
            'cuisine_type': 'Cuisine Type',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image URL',
        }
        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space.',
            'cooking_time': 'Provide the cooking time in minutes.',
        }
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'ingredient1, ingredient2, ...',
            }),
            'instructions': forms.Textarea(attrs={
                'placeholder': 'Enter detailed instructions here...',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        # Validate title length
        if len(title) < 10:
            raise forms.ValidationError("Title must be at least 10 characters long!")

        # Validate unique title
        if Recipe.objects.filter(title=title).exists():
            raise forms.ValidationError("We already have a recipe with the same title!")

        return title


class CreateRecipeForm(RecipeBaseForm):
    pass
