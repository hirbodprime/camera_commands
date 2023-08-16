from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseRedirect
from .models import CommandsModel
from .forms import GenerateCommandForm

def all_commands_view(req):
    command = CommandsModel.objects.all()
    context = {
        'command':command,
    }

    return render(req,'command.html',context)

from django.contrib.sessions.models import Session

from django.urls import reverse_lazy

class CommandGenerateFormView(CreateView):
    template_name = 'generate_command_form.html'
    form_class = GenerateCommandForm
    success_url = reverse_lazy('generate_command')

    def form_valid(self, form):
        self.object = form.save()
        generated_command = f"""
            wbmode={self.object.wbmode}, 
            saturation={self.object.saturation},
            sensor_id={self.object.sensor_id},
            exposuretime={self.object.exposuretime},
            gain={self.object.gain},
            ispdigitalgain={self.object.ispdigitalgain},
            tnr_mode={self.object.tnr_mode},
            ee_mode={self.object.ee_mode},
            aeantibanding={self.object.aeantibanding},
            exposurecompensation={self.object.exposurecompensation},
            aelock={self.object.aelock},
            awblock={self.object.awblock},
            """
        self.request.session['generated_command'] = generated_command
        self.request.session.modified = True
        return super().form_valid(form)

