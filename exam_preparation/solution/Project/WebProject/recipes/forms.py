from django import forms
from WebProject.recipes.models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('author',)

        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': "Optional image URL here..."}
            ),
            'ingredients': forms.Textarea(
                attrs={'placeholder': "ingredient1, ingredient2, ..."}
            ),
            'instructions': forms.Textarea(
                attrs={'placeholder': "Enter detailed instructions here..."}
            )
        }
        error_messages = {
            'title': {
                'unique': "We already have a recipe with the same title!",
            }
        }
        help_texts = {
            'ingredients': "Ingredients must be separated by a comma and space.",
            'cooking_time': "Provide the cooking time in minutes.",


        }


class DeleteRecipeForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


