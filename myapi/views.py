from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    apiurls = {
        
        '/owner_list/': 'owner list and to add owner',
        '/owner_detail/<str:pk>': 'owner detail',
        '/hh_list/': 'Home list',
        '/hh_detail/<str:pk>/': 'Home Detail',
        '/room_list/': 'Room List',
        '/room_detail/<str:pk>/': 'Room Detail'

    }
    return Response(apiurls)

@api_view(['GET', 'POST'])
@csrf_exempt
def owner_list(request):
    if request.method == 'GET':
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'GET':
        serializer = OwnerSerializer(owner)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        owner.delete()
        return Response({}, status=204)
    

@api_view(['GET', 'POST'])
@csrf_exempt
def hh_list(request):
    if request.method == 'GET':
        hhs = HH.objects.all()
        serializer = HHSerializer(hhs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HHSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def hh_detail(request, pk):
    hh = get_object_or_404(HH, pk=pk)
    if request.method == 'GET':
        serializer = HHSerializer(hh)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HHSerializer(hh, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        hh.delete()
        return Response({}, status=204)
    

@api_view(['GET', 'POST'])
@csrf_exempt
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        room.delete()
        return Response({}, status=204)    