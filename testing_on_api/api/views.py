from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import API
from .serializers import APISerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_api(request, pk):
    try:
        api_data = API.objects.get(pk=pk)
    except API.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = APISerializer(api_data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        api_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = APISerializer(api_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_api(request):
    if request.method == 'GET':
        api_data = API.objects.all()
        serializer = APISerializer(api_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'position': request.data.get('position'),
            'company': request.data.get('company')
        }
        serializer = APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
