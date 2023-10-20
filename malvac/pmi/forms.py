from django import forms 
from django.contrib.auth.models import User
from .models import Community


class UserForm(forms.Form):
	communities = forms.ModelMultipleChoiceField(
        queryset=Community.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Make it optional
    )
	class Meta:
		model = User 
		fields = ('username', 'password',)