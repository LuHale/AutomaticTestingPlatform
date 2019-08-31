from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    remember = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('username')
    #     pwd = cleaned_data.get('password')
    #
    #     if User.objects.filter(name=name, pwd=pwd).exists():
    #         return cleaned_data
    #     else:
    #         raise forms.ValidationError('用户名或密码错误，请重新输入')

