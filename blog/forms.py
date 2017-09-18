from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(ModelForm):
    """Form definition for Post."""

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        localized_fields = ('text',)
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        

    

    
        



    

