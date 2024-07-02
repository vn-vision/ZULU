from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users, Properties, Neighborhoods, MarketTrends, UserFeedback, Predictions, PropertyImages
from .serializers import UserSerializer, PropertySerializer, NeighborhoodSerializer, MarketTrendSerializer, UserFeedbackSerializer, PredictionsSerializer, PropertyImagesSerializer
# from .permissions import IsAdminOrReadOnly


# index view, improve on it
def api_index(request):
    return JsonResponse({"Greeting" :"Hello, world. You're at the zulu index."})


# class based view for user
class UserView(APIView):
    '''
    Class based view for the user model.
    It handles the GET, POST, PATCH and DELETE request.
    '''

    # adding permission to the view
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, id=None):
        # get a single user by id
        if id:
            result = get_object_or_404(Users, id=id)

            # check object level permission
            self.check_object_permissions(request, result)
            serializer = UserSerializer(result)
            return Response({'status':'success', 'users':serializer.data}, status=status.HTTP_200_OK)
        
        result = Users.objects.all()
        serializers = UserSerializer(result, many=True)   
        return Response({'status': 'success', 'users': serializers.data}, status=status.HTTP_200_OK)


    def post(self, request):
        '''
        Create a new user record.
        '''
        # check for staff permissions before creating a new user
        if not request.user.is_staff:
            return Response({'status':'error', 'message':'You do not have permission to create a new user'}, status=status.HTTP_403_FORBIDDEN) 
        
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
        # check for permissions before deleting a user
        if not request.user.is_staff:
            return Response({'status':'error', 'message':'You do not have permission to delete a user'}, status=status.HTTP_403_FORBIDDEN)

        # delete a record <id> if it exists
        result = get_object_or_404(Users, id=id)
        result.delete()
        return Response({"status":"success", "data":"Record deleted"}, status=status.HTTP_204_NO_CONTENT)

# class based view for properties
class PropertyView(APIView):
    '''
    Class based view for the property model.
    It handles the GET, POST, PATCH and DELETE request.
    '''
    
    def get(self, request, id=None):
        # get a single property by id
        if id:
            result = get_object_or_404(Properties, id=id)
            serializer = PropertySerializer(result)
            return Response({'status':'success', 'properties':serializer.data}, status=status.HTTP_200_OK)
        
        result = Properties.objects.all()
        serializers = PropertySerializer(result, many=True)   
        return Response({'status': 'success', 'properties': serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create a new property record.
        '''
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        #update  a property with the id <id>
        '''
        Fetch the given id record that is to be update.
        Pass to the StudentSerializer to convert into JSON.
        The data received from the request.
        The partial=True indicates that this may not contains all the fields of our Student model.
        '''
        result = get_object_or_404(Properties, id=id)
        serializer = PropertySerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        # delete a record <id> if it exists
        result = get_object_or_404(Properties, id=id)
        result.delete()
        return Response({"status":"success", "data":"Record deleted"}, status=status.HTTP_204_NO_CONTENT)


# class based view for Neighborhood
class NeighborhoodView(APIView):
    '''
    Class based view for the neighborhood model.
    It handles the GET, POST, PATCH and DELETE request.
    '''
    
    def get(self, request, id=None):
        # get a single neighborhood by id
        if id:
            result = get_object_or_404(Neighborhoods, id=id)
            serializer = NeighborhoodSerializer(result)
            return Response({'status':'success', 'neighborhoods':serializer.data}, status=status.HTTP_200_OK)
        
        result = Neighborhoods.objects.all()
        serializers = NeighborhoodSerializer(result, many=True)   
        return Response({'status': 'success', 'neighborhoods': serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create a new neighborhood record.
        '''
        serializer = NeighborhoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        #update  a neighborhood with the id <id>
        '''
        Fetch the given id record that is to be update.
        Pass to the StudentSerializer to convert into JSON.
        The data received from the request.
        The partial=True indicates that this may not contains all the fields of our Student model.
        '''
        result = get_object_or_404(Neighborhoods, id=id)
        serializer = NeighborhoodSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        # delete a record <id> if it exists
        result = get_object_or_404(Neighborhoods, id=id)
        result.delete()
        return Response({"status":"success", "data":"Record deleted"}, status=status.HTTP_204_NO_CONTENT)
    

class UserFeedbackView(APIView):
    '''
    Class based view for the user feedback model.
    It handles the GET, POST, PATCH and DELETE request.
    '''

    def get(self, request, id=None):
        # get a single user feedback by id
        if id:
            result = get_object_or_404(UserFeedback, id=id)
            serializer = UserFeedbackSerializer(result)
            return Response({'status':'success', 'user_feedback':serializer.data}, status=status.HTTP_200_OK)
        
        result = UserFeedback.objects.all()
        serializers = UserFeedbackSerializer(result, many=True)   
        return Response({'status': 'success', 'user_feedback': serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create a new user feedback record.
        '''
        serializer = UserFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PropertyImagesView(APIView):
    '''
    Class based view for the property images model.
    It handles the GET, POST, PATCH and DELETE request.
    '''

    def get(self, request, id=None):
        # get a single property image by id
        if id:
            result = get_object_or_404(PropertyImages, id=id)
            serializer = PropertyImagesSerializer(result)
            return Response({'status':'success', 'property_images':serializer.data}, status=status.HTTP_200_OK)
        
        result = PropertyImages.objects.all()
        serializers = PropertyImagesSerializer(result, many=True)   
        return Response({'status': 'success', 'property_images': serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        Create a new property image record.
        '''
        serializer = PropertyImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        #update  a property image with the id <id>
        '''
        Fetch the given id record that is to be update.
        Pass to the StudentSerializer to convert into JSON.
        The data received from the request.
        The partial=True indicates that this may not contains all the fields of our Student model.
        '''
        result = get_object_or_404(PropertyImages, id=id)
        serializer = PropertyImagesSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        # delete a record <id> if it exists
        result = get_object_or_404(PropertyImages, id=id)
        result.delete()
        return Response({"status":"success", "data":"Record deleted"}, status=status.HTTP_204_NO_CONTENT)
    

# Market trends view
class MarketTrendView(APIView):
    '''
    Class based view for the market trend model.
    It handles the GET request for the different market redords and trends
    '''

    def get(self, request, id=None):
        # get a single market trend by id
        if id:
            result = get_object_or_404(MarketTrends, id=id)
            serializer = MarketTrendSerializer(result)
            return Response({'status':'success', 'market_trends':serializer.data}, status=status.HTTP_200_OK)
        
        result = MarketTrends.objects.all()
        serializers = MarketTrendSerializer(result, many=True)   
        return Response({'status': 'success', 'market_trends': serializers.data}, status=status.HTTP_200_OK)
    

# Predictions view
class PredictionsView(APIView):
    '''
    Class based view for the predictions model.
    It handles the GET request for the different predictions
    '''

    def get(self, request, property_id=None, neighborbood_id=None):
        # get a single prediction by property_id or neighborhood_id
        if property_id:
            # Fetch predictions related to a specific property
            result = get_object_or_404(Predictions, id=property_id)
            serializer = PredictionsSerializer(result)
            return Response({'status':'success', 'predictions':serializer.data}, status=status.HTTP_200_OK)
        
        if neighborbood_id:
            # Fetch predictions related to a specific neighborhood
            result = get_object_or_404(Predictions, id=neighborbood_id)
            serializer = PredictionsSerializer(result)
            return Response({'status':'success', 'predictions':serializer.data}, status=status.HTTP_200_OK)
        
        result = Predictions.objects.all()
        serializers = PredictionsSerializer(result, many=True)   
        return Response({'status': 'success', 'predictions': serializers.data}, status=status.HTTP_200_OK)