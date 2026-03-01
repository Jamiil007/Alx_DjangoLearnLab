from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register
from . import views

urlpatterns = [
    # Books views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
    path('register/', register, name='register'),

    # Permission-protected Book views
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/', views.edit_book, name='edit_book'),
    path('delete-book/', views.delete_book, name='delete_book'),
]