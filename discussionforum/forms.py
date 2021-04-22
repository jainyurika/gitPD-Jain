from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Post, Comment

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','description']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Post Title'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Post description goes here...'})
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['description']
        widgets = {'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Post a Comment...','rows':'2'})}