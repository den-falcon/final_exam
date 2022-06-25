from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

User = get_user_model()


class AuthUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthUserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'error_messages':
                self.fields[field].widget.attrs.update(
                    {
                        'class': 'form-control',
                        'placeholder': self.fields[field].label
                    }
                )


class AuthUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'phone', 'birth_date', 'avatar',)
        field_classes = {'username': UsernameField}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone",)
