from rest_framework import serializers
from .models import Users, Properties, Neighborhoods, MarketTrends, UserFeedback, PropertyImages, Predictions

class UserSerializer(serializers.ModelSerializer):
    '''
    UserSerializer Class for the user model
    '''
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=100, required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Users
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `User` instance, given the validated data.
        '''
        return Users.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `User` instance, given the validated data.
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    

# class NeighborhoodsSerializer(serializers.ModelSerializer):
class NeighborhoodSerializer(serializers.ModelSerializer):
    '''
    NeighborhoodsSerializer Class for the neighborhoods model
    '''
    name = serializers.CharField(max_length=100, required=True)
    city = serializers.CharField(max_length=100, required=True)
    state = serializers.CharField(max_length=100, required=True)
    avg_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    sales_volumes = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Neighborhoods
        fields = '__all__' 
    

    def create(self, validated_data):
        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.avg_price = validated_data.get('avg_price', instance.avg_price)
        instance.sales_volumes = validated_data.get('sales_volumes', instance.sales_volumes)
        instance.save()
        return instance

# class PropertiesSerializer(serializers.ModelSerializer):
class PropertySerializer(serializers.ModelSerializer):
    '''
    PropertiesSerializer Class for the properties model
    '''
    title = serializers.CharField(max_length=100, required=True)
    address = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    bedrooms = serializers.IntegerField(required=True)
    bathrooms = serializers.IntegerField(required=True)
    neighborhood_id = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Properties
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `Properties` instance, given the validated data.
        '''
        return Properties.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `Properties` instance, given the validated data.
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.address = validated_data.get('address', instance.address)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
        instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
        instance.neighborhood_id = validated_data.get('neighborhood_id', instance.neighborhood_id)
        instance.save()
        return instance
    

# class MarketTrendsSerializer(serializers.ModelSerializer):
class MarketTrendSerializer(serializers.ModelSerializer):
    '''
    MarketTrendsSerializer Class for the market trends model
    '''

    location = serializers.CharField(max_length=100, required=True)
    year = serializers.IntegerField(required=True)
    avg_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    sales_volume = serializers.IntegerField(required=True)
    trend_type = serializers.CharField(max_length=100, required=True)
    neighborhoods_id = serializers.CharField(required=True)
    property_id = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = MarketTrends
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `MarketTrends` instance, given the validated data.
        '''
        return MarketTrends.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `MarketTrends` instance, given the validated data.
        '''
        instance.location = validated_data.get('location', instance.location)
        instance.year = validated_data.get('year', instance.year)
        instance.avg_price = validated_data.get('avg_price', instance.avg_price)
        instance.sales_volume = validated_data.get('sales_volume', instance.sales_volume)
        instance.trend_type = validated_data.get('trend_type', instance.trend_type)
        instance.neighborhoods_id = validated_data.get('neighborhoods_id', instance.neighborhoods_id)
        instance.property_id = validated_data.get('property_id', instance.property_id)
        instance.save()
        return instance
    
# class UserFeedbackSerializer(serializers.ModelSerializer):
class UserFeedbackSerializer(serializers.ModelSerializer):
    '''
    UserFeedbackSerializer Class for the user feedback model
    '''
    user_id = serializers.CharField(required=True)
    property_id = serializers.CharField(required=True)
    rating = serializers.IntegerField(required=True)
    feedback = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = UserFeedback
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `UserFeedback` instance, given the validated data.
        '''
        return UserFeedback.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `UserFeedback` instance, given the validated data.
        '''
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.property_id = validated_data.get('property_id', instance.property_id)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.save()
    
# class PropertyImagesSerializer(serializers.ModelSerializer):
class PropertyImagesSerializer(serializers.ModelSerializer):
    '''
    PropertyImagesSerializer Class for the property images model
    '''
    property_id = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = PropertyImages
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `PropertyImages` instance, given the validated data.
        '''
        return PropertyImages.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `PropertyImages` instance, given the validated data.
        '''
        instance.property_id = validated_data.get('property_id', instance.property_id)
        instance.image = validated_data.get('image', instance.image)
        instance.save()


class PredictionsSerializer(serializers.ModelSerializer):
    '''
    PredictionsSerializer Class for the predictions model
    '''
    property_id = serializers.CharField(required=True)
    neighborhood_id = serializers.CharField(required=True)
    prediction_type = serializers.CharField(max_length=100, required=True)
    prediction_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    prediction_date = serializers.DateTimeField(required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Predictions
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `Predictions` instance, given the validated data.
        '''
        return Predictions.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `Predictions` instance, given the validated data.
        '''
        instance.property_id = validated_data.get('property_id', instance.property_id)
        instance.neighborhood_id = validated_data.get('neighborhood_id', instance.neighborhood_id)
        instance.prediction_type = validated_data.get('prediction_type', instance.prediction_type)
        instance.prediction_price = validated_data.get('prediction_price', instance.prediction_price)
        instance.prediction_date = validated_data.get('prediction_date', instance.prediction_date)
        instance.save()
