from django import forms
from WebProject.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['bio']

        # widgets = {
        #     'password': forms.PasswordInput(),
        # }
        # help_texts = {
        #     'age': "Age requirement: 21 years and above.",
        # }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ()