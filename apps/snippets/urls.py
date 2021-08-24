from django.urls import path

from .views import SnippetDetailView, SnippetListView

app_name = 'snippets'

urlpatterns = [
    path('', SnippetListView.as_view(), name='list'),
    path('<int:pk>/', SnippetDetailView.as_view(), name='detail'),
]
