from django.views.generic import TemplateView, RedirectView

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.views.generic.edit import FormView
from .forms import MultiUploadFileForm
from django.urls import reverse

# Create your views here.
class HomeView(TemplateView, FormView):
    template_name = 'base_app/home.html'
    form_class = MultiUploadFileForm
#    def get_context_data(self, **kwargs):
#        get_unit_id = TblVariable.objects.using('vforwater').select_related('unit').values_list('variable_name', 'variable_symbol')
#        all_variable_names = get_unit_id.values('variable_name', 'variable_symbol','unit__unit_symbol')
#        return {'all_names': all_variable_names}
        
    def get_context_data(self, **kwargs):
        form_class = MultiUploadFileForm
        return {'upload_form': form_class}
 
    
    #success_url = 'views.Login.as_view()' 
    success_url = 'home' 
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print('form: '+str(form));
        files = request.FILES.getlist('file_field')
        print('files: '+str(files));
        if form.is_valid():
            for f in files:
                print('if '+str(f));  # Do something with each file.
            return self.get(request)
        else:
            print('else '+str(files));
            return self.form_invalid(form)
   
        
class Login(TemplateView):
    template_name = 'base_app/login.html'
