from django import forms
from fApp.models import Comment
# create your form vie here.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
