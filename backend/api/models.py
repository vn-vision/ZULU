from django.db import models

# Create your models here.
class Users(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    

class Neighborhoods(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_volumes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' : ' + self.city
class Properties(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    neighborhood_id = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' : ' + self.description

class MarketTrends(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)
    year = models.IntegerField()
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_volume = models.IntegerField()
    trend_type = models.CharField(max_length=100)
    neighborhoods_id = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trend_type + ' : ' + self.location + ' : ' + self.year
    
class UserFeedback(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating + ' : ' + self.feedback

class PropertyImages(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_url.name

class Predictions(models.Model):
    id =  models.CharField(max_length=100, primary_key=True)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE)
    prediction_type = models.CharField(max_length=100)
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)
    predicted_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.predicted_price + ' : ' + self.predicted_date