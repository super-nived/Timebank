from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('image', 'age', 'phone_number', 'area', 'district', 'state', 'nation')

class RegistrationFormChange(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'
class RedeemForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['time', 'currency']
