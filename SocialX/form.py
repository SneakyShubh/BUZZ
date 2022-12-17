from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile_Pic
        fields=("username","image")
    # def __init__(self, *args, **kwargs): 
    #     super(ImageForm, self).__init__(*args, **kwargs)                       
    #     self.fields['username'].disabled = True