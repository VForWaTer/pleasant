from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import MultiUploadFileForm

# Create your views here.
class HomeView(TemplateView, FormView):
    template_name = 'base_app/home.html'
    form_class = MultiUploadFileForm
    file_list = []

#    def get_context_data(self, **kwargs):
#        get_unit_id = TblVariable.objects.using('vforwater').select_related('unit').values_list('variable_name', 'variable_symbol')
#        all_variable_names = get_unit_id.values('variable_name', 'variable_symbol','unit__unit_symbol')
#        return {'all_names': all_variable_names}
        
    def get_context_data(self, **kwargs):
        return {'upload_form': self.form_class, 'file_list': self.file_list}

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file_field')
        self.file_list.append(files)
        return self.get(request)
   
        
class Login(TemplateView):
    template_name = 'base_app/login.html'
