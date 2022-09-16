from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restapi.models import Data
from restapi.api.serializers import DataSerializer

@api_view(['GET','POST'])
def data_list_create_api_view(request):
    if request.method == 'GET':
        datalar = Data.objects.all()
        serializer = DataSerializer(datalar, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def data_detail_api_view(request, pk):
    try:
        data_instance = Data.objects.filter(pk=pk)#instance oluşturuyoruz
    except Data.DoesNotExist:
        return Response(
            {
                'errors':{
                    'code' : 404 ,
                    'message' : f'Böyle bir id({pk})li data yok.'
                }
            },
            status=HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer =  DataSerializer(data_instance, many= True)#serializer için birdern çok queryset pk'ye uygun
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = DataSerializer(data_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data_instance.delete()
        return Response(
            {'islem':{
                'code':204,
                'message':f'({pk}) data deleted'
            }}
            ,status.HTTP_204_NO_CONTENT
            )