from django.contrib import admin
from django.urls import path

from entries.views import LogView, RulesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LogView.as_view(), name='log-view'),
    path('rules', RulesView.as_view(), name='rules-list'),
]
