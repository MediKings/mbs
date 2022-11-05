from django import forms
from home.models import Serie


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        exclude = ['slug', 'date']
