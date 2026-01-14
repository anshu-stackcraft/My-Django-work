from django.shortcuts import render
from django.http import HttpResponse

def master(request):  

    master = [
        {'id': 1, 'name':"anshu" ,"age": 23}
    ]
    

    return HttpResponse( master )