from django.shortcuts import render
from . models import Address
from django.http import JsonResponse
from . serializer import AddressSerilaizer
def index(request):
    address=Address.objects.all()
    serilaizer=AddressSerilaizer(address, many=True)
    return JsonResponse(serilaizer.data, safe=False)