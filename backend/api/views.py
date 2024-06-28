from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer

# class based view for user
class UserView(APIView):
    '''
    Create get and post methods for a user 
    '''
    def get(self, request, *args, **kwargs):
        result = Users.objects.all()
        serializers = UserSerializer(result, many=True)    
        return Response({'status': 'success', 'users': serializers.data}, status=200)


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# index view, improve on it
def api_index(request):
    return JsonResponse({"Greeting" :"Hello, world. You're at the zulu index."})

