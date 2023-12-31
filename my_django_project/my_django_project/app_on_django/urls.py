from django.urls import path

from .views import AuthorView, AddAuthorView, AddQuoteView, AddTagView, QuoteListView, FilterListView, BindTagView, sync

app_name = 'quotes_and_autors_app'

urlpatterns = [
    path('', QuoteListView.as_view(), name='main'),
    path('adding_author/', AddAuthorView.as_view(), name='adding_author'),
    path('adding_quote/', AddQuoteView.as_view(), name='adding_quote'),
    path('adding_tag/', AddTagView.as_view(), name='adding_tag'),
    path('bind_tags/', BindTagView.as_view(), name='bind_tags'),
    path('tag/<str:tag>/', FilterListView.as_view(), name='tag'),
    path('author/<str:author>/', AuthorView.as_view(), name='author'),
    path('sync/', sync, name='sync'),
]
