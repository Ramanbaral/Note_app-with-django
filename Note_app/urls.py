from django.urls import path
from .views import NoteUpdateFrom
from . import views

urlpatterns=[
    path("notes/",views.index,name='note-home'),
    path('delete/<int:pk>/notes/',views.delete,name='note-delete'),
    path('update/<int:pk>',NoteUpdateFrom.as_view(),name='note-update'),
    path('search/',views.search,name='search')
]