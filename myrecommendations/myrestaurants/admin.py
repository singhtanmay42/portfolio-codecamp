from django.contrib import admin
from .models import Restaurant
from .models import Dish
from .models import Review
from .models import RestaurantReview
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)