from django.db import models
from ordered_model.models import OrderedModel


class Rule(OrderedModel):
    """Represents a subreddit rule to which a moderator action may be link."""
    name = models.CharField(max_length=255, help_text='The name of the rule')
    description = models.TextField(blank=True, default='', help_text='Text to further explain or define the rule')
