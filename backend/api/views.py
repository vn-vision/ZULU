from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer

# class based view for user
class UserView(APIView):
    '''
    Class based view for the user model.
    It handles the GET, POST, PATCH and DELETE request.
    '''

    def get(self, request, id=None):
        # get a single user by id
        if id:
            result = get_object_or_404(Users, id=id)
            serializer = UserSerializer(result)
            return Response({'status':'success', 'users':serializer.data}, status=status.HTTP_200_OK)
        
        result = Users.objects.all()
        serializers = UserSerializer(result, many=True)   
        return Response({'status': 'success', 'users': serializers.data}, status=status.HTTP_200_OK)


    def post(self, request):
        '''
        Create a new user record.
        '''
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        #update  a user with the id <id>
        '''
        Fetch the given id record that is to be update.
        Pass to the StudentSerializer to convert into JSON.
        The data received from the request.
        The partial=True indicates that this may not contains all the fields of our Student model.
        '''
        result = get_object_or_404(Users, id=id)
        serializer = UserSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        # delete a record <id> if it exists
        result = get_object_or_404(Users, id=id)
        result.delete()
        return Response({"status":"success", "data":"Record deleted"}, status=status.HTTP_204_NO_CONTENT)


# index view, improve on it
def api_index(request):
    return JsonResponse({"Greeting" :"Hello, world. You're at the zulu index."})



    
