from rest_framework import serializers
from restaurent.models import Restaurant, FoodItem

class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id','name','create_on')
        read_only_field = ('id',)

class RestaurantSerializer(serializers.ModelSerializer):
    food_items = FoodItemsSerializer(many=True, source='fooditem_set')
    class Meta:
        model = Restaurant
        fields = ('id','name','address','phone','food_items')
        read_only_field = ('id',)