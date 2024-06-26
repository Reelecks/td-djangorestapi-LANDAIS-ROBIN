from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    
    path('chercheurs/', views.chercheurs_list, name='chercheurs_list'),
    path('chercheurs/add/', views.add_chercheur, name='add_chercheur'),
    path('chercheurs/edit/<int:id>/', views.edit_chercheur, name='edit_chercheur'),
    path('chercheurs/delete/<int:id>/', views.delete_chercheur, name='delete_chercheur'),
    
    path('projets/', views.projets_list, name='projets_list'),
    path('projets/add/', views.add_projet, name='add_projet'),
    path('projets/edit/<int:id>/', views.edit_projet, name='edit_projet'),
    path('projets/delete/<int:id>/', views.delete_projet, name='delete_projet'),
    
    path('publications/', views.publications_list, name='publications_list'),
    path('publications/add/', views.add_publication, name='add_publication'),
    path('publications/edit/<int:id>/', views.edit_publication, name='edit_publication'),
    path('publications/delete/<int:id>/', views.delete_publication, name='delete_publication'),
    
    path('search/', views.search, name='search'),
    
    
    # API routes
    path('api/chercheurs/', views.chercheurs_list_create_api, name='chercheurs_list_create_api'),
    path('api/chercheurs/<int:pk>/', views.chercheur_detail_api, name='chercheur_detail_api'),

    path('api/projets/', views.projets_list_create_api, name='projets_list_create_api'),
    path('api/projets/<int:pk>/', views.projet_detail_api, name='projet_detail_api'),

    path('api/publications/', views.publications_list_create_api, name='publications_list_create_api'),
    path('api/publications/<int:pk>/', views.publication_detail_api, name='publication_detail_api'),

]
