from django import forms
from .models import Prescription


class ImageForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        labels = {'Photo':''}

