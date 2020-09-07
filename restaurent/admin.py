from django.contrib import admin

from restaurent.models import Restaurant, FoodItem

class FoodItemInline(admin.StackedInline):
    model = FoodItem
    extra = 0

@admin.register(Restaurant)
class RastaurantAdmin(admin.ModelAdmin):
    list_display = ['name','address']
    inlines = [FoodItemInline]



@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name']