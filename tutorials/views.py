from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, permissions
from rest_framework.renderers import JSONRenderer

from .models import Tutorials
from .serializers import TutorialSerializers
from django.core import serializers

from rest_framework.decorators import api_view, permission_classes, renderer_classes


# Create your views here.
@api_view( [ 'GET' ] )
def tutorial_list( request ):
    if request.method == 'GET':
        tutorial = Tutorials.objects.all()
        
        title = request.query_params.get( 'title', None )
        if title is not None:
            tutorial = tutorial.filter( title__contain=title )
        
        tutorial_serializer = TutorialSerializers( tutorial, many=True )
        return JsonResponse( tutorial_serializer.data, safe=False )


@api_view( [ 'POST' ] )
def create_tutorial( request ):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse( request )
        tutorial_serializer = TutorialSerializers( data=tutorial_data )
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse( tutorial_serializer.data, status = status.HTTP_201_CREATED )
        return JsonResponse( tutorial_serializer.errors, status = status.HTTP_400_BAD_REQUEST )


@api_view( [ 'DELETE' ] )
def delete_tutorial( request, pk ):
    if request.method == 'DELETE':

        tutorial = Tutorials.objects.filter( id = pk )
        
        if not tutorial:
            return JsonResponse( {"mensaje": "tutorial no encontrado!!!" }, status = status.HTTP_404_NOT_FOUND )        

        tutorial_serial = serializers.serialize( 'json', list(tutorial), fields=( 'title', 'description', 'published' ) )
        
        tutorial.delete()
        
        return JsonResponse( { "mensaje": "eliminacion exitosa!!!", "tutorial": tutorial_serial  }, status = status.HTTP_202_ACCEPTED )

    return JsonResponse( tutorial_serializer.errors, status = status.HTTP_400_BAD_REQUEST )


@api_view( [ 'PUT' ] )
def update_tutorial( request, pk ):
    if request.method == 'PUT':
        tutorial = Tutorials.objects.filter( id = pk ).first()
        tutorial_serial = TutorialSerializers( tutorial, data=request.data )
        # tutorial_serial = serializers.serialize( 'json', list(tutorial), fields=( 'title', 'description', 'published' ) )
        if tutorial_serial.is_valid():
            tutorial_serial.save()
            return JsonResponse( tutorial_serial.data , status=status.HTTP_200_OK )


@api_view( [ 'GET' ] )
def tutorial_detail( request, pk ):
    try:
        tutorial = Tutorials.objects.filter( id = pk ).first()
        tutorial_serial = TutorialSerializers( tutorial, data=request.data )
        # tutorial_serial = serializers.serialize( 'json', list(tutorial), fields=( 'title', 'description', 'published' ) )
        if tutorial_serial.is_valid():
            return JsonResponse( tutorial_serial.data , status=status.HTTP_200_OK )
    except Tutorials.DoesNoExist:
        return JsonResponse( { 'msj':'el tutorial No existe' }, status=status.HTTP_404_NOT_FOUND )


@api_view(['GET'])
def hello_world(request):
    return JsonResponse({"msj": "Hola hacker!!"}, status=status.HTTP_200_OK)
