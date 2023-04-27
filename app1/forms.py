from django import forms
from app1.models import *
class TopiForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'