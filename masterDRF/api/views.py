from django.shortcuts import render
from django.http import JsonResponse
from master.models import Master



def studentsView(request):
         
                        
    masters = Master.objects.all()
    masters_list = list(masters.values())

    return JsonResponse(masters_list, safe=False)