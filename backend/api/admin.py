from django.contrib import admin
from .models import Users, Neighborhoods, Properties, MarketTrends, UserFeedback, Predictions, PropertyImages

# Register your models here.
admin.site.register(Users)
admin.site.register(Neighborhoods)
admin.site.register(Properties)
admin.site.register(MarketTrends)
admin.site.register(UserFeedback)
admin.site.register(Predictions)
admin.site.register(PropertyImages)