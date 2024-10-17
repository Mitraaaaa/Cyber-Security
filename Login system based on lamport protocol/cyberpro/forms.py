from django import forms
from .models import UserProfile
import hashlib
from django import forms


def lamport_hash(n, value):
    hashed_value = hashlib.sha256(str(value).encode()).hexdigest()
    for _ in range(n - 1):
        hashed_value = hashlib.sha256(hashed_value.encode()).hexdigest()
    return hashed_value


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = lamport_hash(user.n_value, self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
