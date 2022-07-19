from django import forms  
from .validator import validate_me

class uploadvideo(forms.Form):  
    file      = forms.FileField(widget = forms.FileInput(attrs={'id':'file_id'}),required=True,validators=[validate_me])
    