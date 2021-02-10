from django import forms
from django.core.exceptions import ValidationError

from entries.models import Entry


class EntryForm(forms.ModelForm):
    ban_length = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        ban_length = cleaned_data.get('ban_length')
        action = cleaned_data.get('action')

        if action == Entry.ACTION_TEMP_BAN and not ban_length:
            raise ValidationError('Ban Length is required for temporary bans.')

    class Meta:
        model = Entry
        fields = [
            'user',
            'rule',
            'action',
            'ban_length',
            'notes',
        ]
