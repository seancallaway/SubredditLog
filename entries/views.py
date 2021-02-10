from django.views.generic import ListView

from entries.models import Entry, Rule


class LogView(ListView):
    template_name = 'entries/log.html'
    model = Entry
    context_object_name = 'entries'
    queryset = Entry.objects.all()


class RulesView(ListView):
    template_name = 'entries/rules.html'
    model = Rule
    context_object_name = 'rules'
    queryset = Rule.objects.all()
