from django.views.generic import DetailView, ListView

from .models import Snippet


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/detail.html'
    context_object_name = 'snippet'


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/list.html'
    context_object_name = 'snippets'
