from django import forms
from .models import Klient


class KlientForm(forms.ModelForm):
    # name = forms.CharField(label='Imię: ')
    # surname = forms.CharField(label='Nazwisko: ')
    # birth_date = forms.DateField(label='Data urodzenia: ')
    # email = forms.CharField(label='Email: ' )
    # phone_number = forms.IntegerField(label='Numer telefonu: ')
    # login = forms.CharField(label='Login: ')
    # password = forms.CharField(label='Hasło: ')

    class Meta:
        model = Klient
        fields = [
            'imie',
            'nazwisko',
            'data_urodzenia',
            'email',
            'telefon',
            'login',
            'haslo',
            'miasto',
            'kod_pocztowy',
            'ulica',
            'lokal',
            'kraj',
        ]
