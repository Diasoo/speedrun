from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'speedrun_app/about/about.html'