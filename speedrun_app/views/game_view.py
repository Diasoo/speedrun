from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from speedrun_app.models import Game
from speedrun_app.forms import GameForm



class GameListView(ListView):
    model = Game
    template_name = 'speedrun_app/game/game_list.html'
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GameDetailView(DetailView):
    model = Game
    template_name = 'speedrun_app/game/game_detail.html'
    context_object_name = 'game'

class GameCreateView(CreateView):
    model = Game
    template_name = 'speedrun_app/game/game_form.html'
    form_class = GameForm
    success_url = reverse_lazy('game_list')

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'speedrun_app/game/game_form.html'
    form_class = GameForm
    success_url = reverse_lazy('game_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context

class GameDeleteView(View):
    def post(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        game.delete()
        return HttpResponseRedirect(reverse('game_list'))