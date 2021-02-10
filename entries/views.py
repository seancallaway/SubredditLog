from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

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


class AddEntryView(LoginRequiredMixin, CreateView):
    template_name = 'entries/add_entry.html'
    model = Entry
    fields = [
        'user',
        'rule',
        'action',
        'ban_length',
        'notes',
    ]

    def form_valid(self, form):
        form.instance.mod = self.request.user
        return super().form_valid(form)
