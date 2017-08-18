from django.views.generic import TemplateView

from django.shortcuts import render
from base_app.models import UploadedFile

# Create your views here.
class Workbench(TemplateView):
    template_name = 'pleasant_wps/app_home.html'
    
    def get(self, request):
        data_list = UploadedFile.objects.all()
        return render(self.request, 'pleasant_wps/app_home.html', {'data': data_list})
    
    def post(self, request):
        form = DataForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save()
            data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

class Login(TemplateView):
    template_name = 'base_app/login.html'
    
    
    # TODO: Brauch ne Datenbank mit der file_list