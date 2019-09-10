from django import forms
from .models import Comment
from .models import Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user','text',)

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
 
        fields = ['title', 'pub_date', 'body']        