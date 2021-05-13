from django.forms import ModelForm, TextInput


class FirstForm(ModelForm):
    widgets = {
        'username': TextInput(attrs={
            'name': 'username',
            'class': 'form-control',
            'placeholder': 'Введите username'
        }),
    }
