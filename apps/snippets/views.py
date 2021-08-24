from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Beat, Hihat, Kick, Pattern, Snare, Snippet
from .serializers import SnippetUpdateSerializer


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/detail.html'
    context_object_name = 'snippet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bars'] = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        return context


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/list.html'
    context_object_name = 'snippets'


class SnippetCreateView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        snippet = Snippet.objects.create(name=name)
        beat = Beat.objects.create(snippet=snippet)
        hihat = Hihat.objects.create(beat=beat)
        snare = Snare.objects.create(beat=beat)
        kick = Kick.objects.create(beat=beat)
        Pattern.objects.create(hihat=hihat)
        Pattern.objects.create(snare=snare)
        Pattern.objects.create(kick=kick)
        return redirect(snippet.get_absolute_url())


class SnippetUpdateAPIView(generics.GenericAPIView):
    serializer_class = SnippetUpdateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pattern_id = serializer.data.get('pattern_id')
        bar = serializer.data.get('bar')
        pattern = Pattern.objects.get(id=pattern_id)
        setattr(pattern, bar, not getattr(pattern, bar))
        pattern.save()
        return Response('OK', status=status.HTTP_200_OK)
