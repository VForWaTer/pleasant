from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import MultiUploadFileForm
from django.template.defaultfilters import length
from pywps.app import WPSRequest
from tests import test_wpsrequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
#from .models import UploadedFile

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base_app/home.html'
#     form_class = MultiUploadFileForm
#     file_list = []
#     file_list_dict = {}
  #  print('the file_list: ', file_list)
  #  print('file_list_dict: ', file_list_dict)

#    def get_context_data(self, **kwargs):
#        get_unit_id = TblVariable.objects.using('vforwater').select_related('unit').values_list('variable_name', 'variable_symbol')
#        all_variable_names = get_unit_id.values('variable_name', 'variable_symbol','unit__unit_symbol')
#        return {'all_names': all_variable_names}
#         
#     def get_context_data(self, **kwargs):
#         return {'upload_form': self.form_class, 'file_list': self.file_list}

#     def post(self, request, *args, **kwargs):
#         files = request.FILES.getlist('file_field')
#    #    print('request.FILES: ', request.FILES)
# 
#         self.file_list.extend(files)
#         self.file_list_dict = (self.file_list_dict, files)
# 
#         return self.get(request)
    
#     def post(self, request, *args, **kwargs):
#         print('request.POST', request.POST)
#         print('request.POST', dir(request.POST))        
#         print('request.POST', request.POST.get('name', ''))
#         print('dict: ', dict(request.POST.lists()))
#         method = getattr(self, 'step_' + request.POST.get('step', ''), self.set_data)
#         return self.get(request)   
# #         return method(request, *args, **kwargs)     
#     
#     def get(self, request):
#         print('get self: ', self)
#         print('get request: ', request)
#         return render(self.request, home.html, self.file_list)
    
#     def set_data(self, request, *args, **kwargs):
#         files = request.FILES.getlist('file_field')
#         self.file_list.extend(files)
#        # print('I am in set data')
#         pass
#         
#     def remove_data(self, *args, **kwargs):
#         #print('remove data; here I am')
#         return {'file_list': self.file_list}
    def get(self, request):
        data_list = UploadedFile.objects.all()
        print('get geht: ', data_list)
        return render(self.request, 'base_app/workspace.html', {'data': data_list})#     
    
from django.http import JsonResponse
from django.views import View
from .forms import DataForm
from .models import UploadedFile

class DataUploadView(View):
    def get(self, request):
        data_list = UploadedFile.objects.all()
        print('get geht: ', data_list)
        return render(self.request, 'base_app/workspace.html', {'data': data_list})
#        return render(self.request, 'base_app/data_access.html', {'data': data_list})
            
    def post(self, request):
        form = DataForm(self.request.POST, self.request.FILES)
        print('im Post', form)
        if form.is_valid():
            file = form.save()
            data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
            print('if post ', file.file.name, ' url ', file.file.url)
        else:
            data = {'is_valid': False}
            print('else post', data)
        return JsonResponse(data)

def clear_database(request):
    print ('clear: ', UploadedFile.objects.all())
    for file in UploadedFile.objects.all():
        file.file.delete()
        file.delete()
    return redirect(request.POST.get('next'))
  
def delete_data(request, pk):
    data = get_object_or_404(UploadedFile, pk=pk)
    print ('in delete / data: ', data)
    if request.method == 'POST':
        form = DataForm(request.POST, instance = data)
    else:
        form = DataForm(instance = data)
    return DataUploadView.get(request)
    for file in UploadedFile.objects.all():
        file.file.delete()
        file.delete()
    return redirect(request.POST.get('next'))


class Login(TemplateView):
    template_name = 'base_app/login.html'
    
    
    
