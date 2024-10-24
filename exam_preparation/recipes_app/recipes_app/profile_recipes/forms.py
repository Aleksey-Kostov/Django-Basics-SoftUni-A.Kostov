from django import forms

from recipes_app.profile_recipes.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']
        labels = {
            'nickname': 'Nickname',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'chef': 'Chef',
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name[0].isupper():
            raise forms.ValidationError("First name must start with a capital letter!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name[0].isupper():
            raise forms.ValidationError("Last name must start with a capital letter!")
        return last_name

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if len(nickname) < 2:
            raise forms.ValidationError("Nickname must be at least 2 chars long!")
        return nickname


class CreateProfileForm(ProfileBaseForm):
    pass
