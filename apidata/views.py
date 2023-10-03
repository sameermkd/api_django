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
@api_view(['GET','PUT','DELETE','PUT'])
def data(request,id):
    try:
        address=Address.objects.get(pk=id)
    except Address.DoesNotExist:
        return JsonResponse({'Error':'Address not found'}, status=404)
    if request.method=='GET':
        serilaizer=AddressSerilaizer(address)
        return JsonResponse(serilaizer.data)
    elif request.method=='PUT':
        serilaizer=AddressSerilaizer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data)
    elif request.method=='DELETE':
        address.delete()
        return JsonResponse({'Deleted':'Address Deleted'}, status=204)
    return JsonResponse()
