from django.test import TestCase

from entries.forms import EntryForm
from entries.models import Entry, Rule


class EntryFormTest(TestCase):

    def setUp(self) -> None:
        self.rule1 = Rule.objects.create(name='Be civil')

    def test_cannot_submit_temp_ban_without_length(self):
        form = EntryForm(data={
            'user': 'thecal714',
            'rule': self.rule1,
            'action': Entry.ACTION_TEMP_BAN,
        })

        self.assertIn(
            'Ban Length is required for temporary bans.',
            form.errors['__all__']
        )
