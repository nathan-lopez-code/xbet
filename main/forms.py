from django import forms


class FormClub(forms.Form):


    number_vise = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-user xvc",
        'placeholder': "Entrer la cote finale a atteindre"
    }))


    cote_equipe_1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-user xvc",
        'placeholder': " premiere combinaison"
    }))

    cote_equipe_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control form-control-user xvc",
            'placeholder': "deuxieme combinaison"
        }
    ))
