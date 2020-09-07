
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
from restaurent.models import Restaurant, FoodItem
from restaurent.serializers import RestaurantSerializer, FoodItemsSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().order_by('-create_on')
    serializer_class = RestaurantSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class FoodItemViewSet(ModelViewSet):
    serializer_class = FoodItemsSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    def get_queryset(self):
        return FoodItem.objects.filter(restaurant_id=self.kwargs['restaurant_pk'])\
            .order_by('-create_on')






# @csrf_exempt
# def restaurant_handler(request):
#     if request.method == 'GET':
#         return list_restaurnat(request)
#     if request.method == 'POST':
#         return create_restaurant(request)
#
# def list_restaurnat(request):
#     query_restaurnt = Restaurant.objects.all()\
#         .order_by('-create_on').\
#         values('name','address','phone')
#     return JsonResponse(
#         list(query_restaurnt),safe=False
#     )
#
#
# def create_restaurant(request):
#     data = json.loads(request.body)
#     obj = Restaurant(name = data['name'], address = data['address'], phone = ['phone'])
#     obj.save()
#     return JsonResponse({
#         'id':obj.id,
#         **data
#     })