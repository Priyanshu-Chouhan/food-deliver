# delivery/urls.py

# from django.urls import path
# from .views import DeliveryCostAPI

# urlpatterns = [
#     path('calculate_delivery_cost/', DeliveryCostAPI.as_view(), 
#         name='calculate_delivery_cost'),
#]
from django.urls import path
from .views import DeliveryViewset

urlpatterns =[
path('delivery/', DeliveryViewset.as_view()),
 path('delivery/<int:id>', DeliveryViewset.as_view())    
     ]
