import json
from django.shortcuts import render
from MainApp.models import Candels
from MainApp.form import CsvUploadForm 
import pandas as pd
from django.http import HttpResponse
from MainApp.utils import candel_create


app = 'MainApp'

def dashbord(request):
    if request.method == 'POST' :
        fm = CsvUploadForm(request.POST,request.FILES)

        if fm.is_valid():
            fm.save()
            csv_data = fm.cleaned_data['csv_file']
            time_frame = fm.cleaned_data['time_frame']
            data_frame = pd.read_csv(csv_data,low_memory=False)
            data = candel_create(data_frame,time_frame)
            result = data.to_json(orient="records")
            parsed = json.loads(result)
            data_json = json.dumps(parsed, indent=4)

            return HttpResponse(data_json)  

    else:
        fm = CsvUploadForm()
    return render(request,f'{app}/uploadfile.html',{'form':fm})


