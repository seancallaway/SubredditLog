from django.views.generic import TemplateView


class LogView(TemplateView):
    template_name = 'entries/log.html'
