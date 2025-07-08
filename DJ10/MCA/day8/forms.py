from django.forms import fields
from .models import studentModel
from django import forms
class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'
