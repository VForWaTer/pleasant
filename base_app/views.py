from django.conf import settings
from django.views.generic import TemplateView

from .forms import MultiUploadFileForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from django.views import View
from .forms import DataForm
from .models import UploadedFile

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base_app/home.html'

    def get(self, request):
        data_list = UploadedFile.objects.all()
        return render(self.request, 'base_app/home.html', {'data': data_list})
        
    def post(self, request):
        form = DataForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save()
            data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
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
    
#     TODO: find better Name for Workspace. Maybe Datarack?
    
