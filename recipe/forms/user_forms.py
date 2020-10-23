from django import forms
from django.utils.translation import gettext_lazy as _
from recipe.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label=_("Your username"), min_length=1, max_length=255)
    password = forms.CharField(
        label=_("Your Password"), min_length=6, max_length=4096
    )

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]