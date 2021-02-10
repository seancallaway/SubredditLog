from django.contrib import admin
from django.urls import path

from entries.views import LogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LogView.as_view(), name='log-view'),
]
