from django.urls import path
from . import views as v
urlpatterns = [
    path('history/', v.all_commands_view,name='command_history'),
    path('generate/', v.CommandGenerateFormView.as_view(),name='generate_command'),
]
