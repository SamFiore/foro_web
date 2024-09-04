from django.forms import ModelForm,TextInput
from .models import PostModel,CommentModel

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ['name_post','txt_post']

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']
        labels = {
            'comment':''
        }
        widgets = {
            'comment': TextInput(attrs={'placeholder':'Put your commentary here'})
        }