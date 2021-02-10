from django.views.generic import ListView

from entries.models import Entry


class LogView(ListView):
    template_name = 'entries/log.html'
    model = Entry
    context_object_name = 'entries'
    queryset = Entry.objects.all()
