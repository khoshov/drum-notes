from django.urls import path

from .views import SnippetDetailView, SnippetListView, SnippetCreateView, SnippetUpdateAPIView

app_name = 'snippets'

urlpatterns = [
    path('', SnippetListView.as_view(), name='list'),
    path('<int:pk>/', SnippetDetailView.as_view(), name='detail'),
    path('add/', SnippetCreateView.as_view(), name='add'),
    path('update/', SnippetUpdateAPIView.as_view(), name='update'),
]
