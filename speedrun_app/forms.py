from django import forms
from speedrun_app.models import CustomUser, Game, Run, Genre

class CustomUserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Heslo')

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

class CustomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Uživatelské jméno')
    password = forms.CharField(widget=forms.PasswordInput, label='Heslo')

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'release_date', 'developer', 'publisher', 'genres']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'genres': forms.CheckboxSelectMultiple(),
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['game', 'user', 'time', 'platform', 'category']
