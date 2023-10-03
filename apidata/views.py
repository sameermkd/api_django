from django.shortcuts import render
from . models import Address
from django.http import JsonResponse
from . serializer import AddressSerilaizer
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def index(request):
    if request.method=="GET":
        address=Address.objects.all()
        serilaizer=AddressSerilaizer(address, many=True)
        return JsonResponse(serilaizer.data, safe=False)
    if request.method=="POST":
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data, safe=False)
    return JsonResponse()