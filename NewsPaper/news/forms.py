from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author',
                  'category',
                  'title',
                  'text',
                  ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title is not None and len(title.split())> 20:
            raise ValidationError({
                "title": "Заголовок не может быть более 20 слов"
            })
        return cleaned_data
