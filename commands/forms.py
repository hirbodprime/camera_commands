from django.forms import ModelForm
from .models import CommandsModel

class GenerateCommandForm(ModelForm):
    class Meta:
        model = CommandsModel
        fields = '__all__'

