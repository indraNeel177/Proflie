from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import messgae
from .serializers import messageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class MessageApiView(APIView):

    def get(self, request):
        message = messgae.objects.all()
        serializer = messageSerializer(message, many=type)
        return Response(serializer.data)

    def post(self, request):
        serializer = messageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetails(APIView):

    def get_object(self, id):
        try:
            message1 = messgae.objects.get(id=id)
            return message1
        except message1.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        message1 = self.get_object(id)
        serializer = messageSerializer(message1)
        return Response(serializer.data)

    def put(self, request, id):
        message1 = self.get_object(id)
        serializer = messageSerializer(message1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        message1 = self.get_object(id)
        message1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == "GET":
        message = messgae.objects.all()
        serializer = messageSerializer(message, many=type)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = messageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def message_edit(request, pk):
    try:
        message1 = messgae.objects.get(pk=pk)
    except message1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = messageSerializer(message1)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = messageSerializer(message1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def Message_list(request):
    if request.method == "GET":
        message = messgae.objects.all()
        serializer = messageSerializer(message, many=type)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = messageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def Message_edit(request, pk):
    try:
        message1 = messgae.objects.get(pk=pk)
    except message1.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = messageSerializer(message1)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = messageSerializer(message1, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        message1.delete()
        return HttpResponse(status=204)

# Create your views here.
