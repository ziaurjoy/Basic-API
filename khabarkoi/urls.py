
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested.routers import SimpleRouter,NestedSimpleRouter
from restaurent.views import RestaurantViewSet, FoodItemViewSet

api_router = SimpleRouter(trailing_slash=False)
api_router.register('restaurant',RestaurantViewSet,basename='restaurant')

restaurant_router = NestedSimpleRouter(api_router,'restaurant',lookup='restaurant')
restaurant_router.register('food_items',FoodItemViewSet,basename='food_item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(api_router.urls)),
    path('api/v1/',include(restaurant_router.urls)),
    path('api/v1/token',obtain_auth_token),

]
