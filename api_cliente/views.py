# Create your views here.
from .serializer import Registro_clienteSerializer
from .models import Registro_cliente
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response

@api_view(['GET'])
def Listar_cliente(request):
    registro_cliente = Registro_cliente.objects.all()
    serializer = Registro_clienteSerializer(registro_cliente, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detalle_cliente(request, pk):
    registro_cliente = Registro_cliente.objects.get(id=pk)
    serializer = Registro_clienteSerializer(registro_cliente, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Registro_cli(request):
    serializer = Registro_clienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['PUT'])
def Actualizar_cliente(request, pk):
    registro_cliente = Registro_cliente.objects.get(id=pk)
    serializer = Registro_clienteSerializer(instance=Registro_cliente, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Eliminar_cliente(request, pk):
    registro_cliente = Registro_cliente.objects.get(id=pk)
    registro_cliente.delete()

    return Response('Eliminado')