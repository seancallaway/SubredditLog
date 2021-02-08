from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from entries.models import Rule


@admin.register(Rule)
class RuleAdmin(OrderedModelAdmin):
    list_display = (
        'order'
        'title',
        'move_up_down_links'
    )

    readonly_fields = (
        'order',
        'move_up_down_links',
    )

    ordering = ('order', )
