from django import forms
from .models import Post
from django.core.exceptions import ValidationError

from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not (5 <= len(title) <= 50):
            raise ValidationError("Title must be between 5 and 50 characters!")

        if Post.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Oops! That title is already taken. How about something fresh and fun!")

        return title


class PostCreationForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        help_texts = {}

    pass


class PostDeleteForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'disabled': 'disabled'}),
            'image_url': forms.TextInput(attrs={'disabled': 'disabled'}),
            'content': forms.Textarea(attrs={'disabled': 'disabled'}),
        }

        help_texts = {}
