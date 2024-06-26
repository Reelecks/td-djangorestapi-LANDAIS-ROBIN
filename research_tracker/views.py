from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Vues API (JSON)
# Chercheurs
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chercheurs_list_create_api(request):
    if request.method == 'GET':
        chercheurs = Chercheur.objects.all()
        serializer = ChercheurSerializer(chercheurs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChercheurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def chercheur_detail_api(request, pk):
    try:
        chercheur = Chercheur.objects.get(pk=pk)
    except Chercheur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChercheurSerializer(chercheur)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ChercheurSerializer(chercheur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        chercheur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Projets de recherche
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def projets_list_create_api(request):
    if request.method == 'GET':
        projets = ProjetDeRecherche.objects.all()
        serializer = ProjetDeRechercheSerializer(projets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjetDeRechercheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def projet_detail_api(request, pk):
    try:
        projet = ProjetDeRecherche.objects.get(pk=pk)
    except ProjetDeRecherche.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjetDeRechercheSerializer(projet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjetDeRechercheSerializer(projet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        projet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Publications
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def publications_list_create_api(request):
    if request.method == 'GET':
        publications = Publication.objects.all()
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def publication_detail_api(request, pk):
    try:
        publication = Publication.objects.get(pk=pk)
    except Publication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublicationSerializer(publication)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PublicationSerializer(publication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Vues HTML
@login_required
def chercheurs_list(request):
    return render(request, 'research_tracker/chercheurs_list.html')

@login_required
def projets_list(request):
    return render(request, 'research_tracker/projets_list.html')

@login_required
def publications_list(request):
    return render(request, 'research_tracker/publications_list.html')

@login_required
def add_chercheur(request):
    if request.method == 'POST':
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chercheurs_list')
    else:
        form = ChercheurForm()
    return render(request, 'research_tracker/add_chercheur.html', {'form': form})

@login_required
def edit_chercheur(request, id):
    chercheur = get_object_or_404(Chercheur, id=id)
    if request.method == 'POST':
        form = ChercheurForm(request.POST, instance=chercheur)
        if form.is_valid():
            form.save()
            return redirect('chercheurs_list')
    else:
        form = ChercheurForm(instance=chercheur)
    return render(request, 'research_tracker/edit_chercheur.html', {'form': form})

@login_required
def delete_chercheur(request, id):
    chercheur = get_object_or_404(Chercheur, id=id)
    if request.method == 'POST':
        chercheur.delete()
        return redirect('chercheurs_list')
    return render(request, 'research_tracker/delete_confirm.html', {'object': chercheur})

@login_required
def add_projet(request):
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projets_list')
    else:
        form = ProjetDeRechercheForm()
    return render(request, 'research_tracker/add_projet.html', {'form': form})

@login_required
def edit_projet(request, id):
    projet = get_object_or_404(ProjetDeRecherche, id=id)
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projets_list')
    else:
        form = ProjetDeRechercheForm(instance=projet)
    return render(request, 'research_tracker/edit_projet.html', {'form': form})

@login_required
def delete_projet(request, id):
    projet = get_object_or_404(ProjetDeRecherche, id=id)
    if request.method == 'POST':
        projet.delete()
        return redirect('projets_list')
    return render(request, 'research_tracker/delete_confirm.html', {'object': projet})

@login_required
def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm()
    return render(request, 'research_tracker/add_publication.html', {'form': form})

@login_required
def edit_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'research_tracker/edit_publication.html', {'form': form})

@login_required
def delete_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        publication.delete()
        return redirect('publications_list')
    return render(request, 'research_tracker/delete_confirm.html', {'object': publication})

@login_required
def search(request):
    search_query = request.GET.get('q', '')
    chercheurs = Chercheur.objects.filter(nom__icontains=search_query) | Chercheur.objects.filter(specialite__icontains=search_query)
    projets = ProjetDeRecherche.objects.filter(titre__icontains=search_query) | ProjetDeRecherche.objects.filter(description__icontains=search_query)
    publications = Publication.objects.filter(titre__icontains=search_query) | Publication.objects.filter(resume__icontains=search_query)

    return render(request, 'research_tracker/search.html', {
        'chercheurs': chercheurs,
        'projets': projets,
        'publications': publications,
        'search_query': search_query,
    })

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response = redirect('chercheurs_list')
            response.set_cookie('access_token', str(refresh.access_token), httponly=False)  # Change httponly to False for testing
            response.set_cookie('refresh_token', str(refresh), httponly=False)  # Change httponly to False for testing
            return response
        else:
            return render(request, 'research_tracker/login.html', {'error': 'Invalid credentials'})
    return render(request, 'research_tracker/login.html')

@login_required
def logout_view(request):
    logout(request)
    response = redirect('login_view')
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = UserCreationForm()
    return render(request, 'research_tracker/register.html', {'form': form})
