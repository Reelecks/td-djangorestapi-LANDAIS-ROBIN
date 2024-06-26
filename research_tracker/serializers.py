from rest_framework import serializers
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chercheur
        fields = ['id', 'nom', 'specialite']

class ProjetDeRechercheSerializer(serializers.ModelSerializer):
    chef_projet = ChercheurSerializer(read_only=True)

    class Meta:
        model = ProjetDeRecherche
        fields = ['id', 'titre', 'description', 'date_debut', 'date_fin_prevue', 'chef_projet']

class PublicationSerializer(serializers.ModelSerializer):
    projet_associe = ProjetDeRechercheSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = ['id', 'titre', 'resume', 'projet_associe', 'date_publication']
