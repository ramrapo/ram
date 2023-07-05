import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Friend Good Evening!!!!</h1><hr>'
    msg=msg+'<h2>Now server time is:'+str(date)+'</h2>'
    return HttpResponse(msg)
