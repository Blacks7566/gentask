from django import forms
from MainApp.models import Candels


class CsvUploadForm(forms.ModelForm):
    class Meta:
        model = Candels
        fields = ['csv_file','time_frame']