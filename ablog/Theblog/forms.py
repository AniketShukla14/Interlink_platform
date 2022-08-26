from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag', 'author', 'body') # 'category', )

        widgets={
            'title': forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Enter the title'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter the title'}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' :'form-control','placeholder':'Enter the body'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag', 'body') 

        widgets={
            'title': forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Enter the title'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter the title'}),
            'body': forms.Textarea(attrs={'class' :'form-control','placeholder':'Enter the body'}),

        }