from myAppProject.models import Upload
from django.forms import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('owner', 'image','desc')

