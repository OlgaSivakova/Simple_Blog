from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy
from django import forms

from .models import Comments, Post

User = get_user_model()
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label=("Email"),
                             max_length=254,
                             widget=forms.EmailInput(attrs={'autocomplete':'email'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments #куда всё вносим в админке
        fields = ('name', 'textcom')
        
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'descript', 'author', 'img']
        
    def clean_descript(self):
        
        title_data = self.cleaned_data['title']
        descript_data = self.cleaned_data['descript']

        if title_data == descript_data:
            raise ValidationError("The title and subtitle should be different")
        
        return descript_data
        