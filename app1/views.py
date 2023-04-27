from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *

# Create your views here.
def insert_topic(request):
    TF=TopiForm()
    d={'TF':TF}
    if request.method=='POST':
        TFD=TopiForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data inserted successfulyyyy')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)
