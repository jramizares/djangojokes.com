from django.urls import path

from .views import (
    JokeCreateView, JokeDeleteView, JokeDetailView, JokeListView, JokeUpdateView, vote
)

app_name = 'jokes'
urlpatterns = [
    path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),
    path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<slug>/', JokeDetailView.as_view(), name='detail'),
    path('joke/<slug>/vote/', vote, name='ajax-vote'),
    path('', JokeListView.as_view(), name='list'),
]