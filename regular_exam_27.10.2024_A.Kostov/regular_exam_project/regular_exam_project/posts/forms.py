from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Share your funniest furry photo URL!'}),
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
        current_post = self.instance
        if Post.objects.filter(title=title).exclude(pk=current_post.pk).exists():
            raise ValidationError("Oops! That title is already taken. How about something fresh and fun!")
        if not (5 <= len(title) <= 50):
            raise ValidationError("Title must be between 5 and 50 characters!")

        return title
