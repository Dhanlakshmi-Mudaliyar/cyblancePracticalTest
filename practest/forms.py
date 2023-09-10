from django import forms
from .models import Person, CustomUser
from django.contrib.auth.forms import UserCreationForm

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ("username", "email", "password1")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user