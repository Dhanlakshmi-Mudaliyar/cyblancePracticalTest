from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

