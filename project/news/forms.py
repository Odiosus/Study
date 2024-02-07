from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            # 'author',
            'category',
            'text',
        ]


class PostFormForStaff(PostForm): 
    PostForm.Meta.fields.append('author')
    
    