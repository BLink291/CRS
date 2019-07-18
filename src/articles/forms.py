from django import forms
from .models import Article

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Article
        template = 'article_new.html'
        fields = ('title' , 'body', 'lat', 'lng')
        widgets = {
            'lat': forms.HiddenInput(),
            'lng': forms.HiddenInput(),
            'slug': forms.HiddenInput()
            }

         
