from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from speedrun_app.models import Run
from speedrun_app.forms import RunForm


class RunListView(ListView):
    model = Run
    template_name = 'speedrun_app/run/run_list.html'
    context_object_name = 'runs'
    ordering = ['-date']

class RunDetailView(DetailView):
    model = Run
    template_name = 'speedrun_app/run/run_detail.html'
    context_object_name = 'run'

class RunCreateView(CreateView):
    model = Run
    form_class = RunForm
    template_name = 'speedrun_app/run/run_form.html'
    success_url = reverse_lazy('run_list')

class RunUpdateView(UpdateView):
    model = Run
    form_class = RunForm
    template_name = 'speedrun_app/run/run_form.html'

    def get_success_url(self):
        return reverse('run_detail', kwargs={'pk': self.object.pk})

class RunDeleteView(View):
    def post(self, request, pk):
        run = get_object_or_404(Run, pk=pk)
        run.delete()
        return HttpResponseRedirect(reverse('run_list'))