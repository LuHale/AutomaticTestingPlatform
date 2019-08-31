from django import forms
from django.contrib.auth.models import User
from .models import UserExtension
from django.core import validators


class RegisterForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, validators=[
        validators.RegexValidator("^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$")])
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_phone_number(self):

        telephone = self.cleaned_data.get('phone_number')
        exists = User.objects.filter(extension__phone_number=telephone).exists()
        if exists:
            raise forms.ValidationError("手机号已经存在")
        return telephone


