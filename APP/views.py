from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NewtonSerializer
from .math import Newton_Method
# Create your views here.

@api_view(['GET', 'POST'])

def Newton(request):
    if request.method == 'GET':
        answer = {
            "equation": "x",
            "first": 200,
            "second": 300
        }
        
        serializer = NewtonSerializer(data=answer)
        serializer.is_valid()
        return Response(serializer.validated_data)
    if request.method == "POST":
        
        serializer = NewtonSerializer(data = request.data)
        serializer.is_valid()
        
        equation = serializer.data['equation']
        first = int(serializer.data['first'])
        second = int(serializer.data['second'])
        
        answer = {Newton_Method(equation, first, second)}
        
        return Response(answer, status=status.HTTP_200_OK)
        
        
