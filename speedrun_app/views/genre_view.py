from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from speedrun_app.models import Genre
from speedrun_app.forms import GenreForm


class GenreListView(ListView):
    model = Genre
    template_name = 'speedrun_app/genre/genre_list.html'
    context_object_name = 'genres'

class GenreCreateView(CreateView):
    model = Genre
    template_name = 'speedrun_app/genre/genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'speedrun_app/genre/genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(View):
    def post(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return HttpResponseRedirect(reverse('genre_list'))

