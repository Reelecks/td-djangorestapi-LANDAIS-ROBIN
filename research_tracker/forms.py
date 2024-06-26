from django import forms
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        fields = '__all__'

class ProjetDeRechercheForm(forms.ModelForm):
    class Meta:
        model = ProjetDeRecherche
        fields = '__all__'

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
