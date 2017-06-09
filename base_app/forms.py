from django import forms

# To upload the file to a model check the django documentation
# https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

class MultiUploadFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True, 
        'id': 'select_data_button2',
        'style': 'display: none',
        'onchange': "this.form.submit()",
        }))

