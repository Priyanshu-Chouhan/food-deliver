# delivery/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pricing
from .serializers import PricingSerializer

class DeliveryViewset(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PricingSerializer(data=data)
        if serializer.is_valid():
            pricing = serializer.save()
            total_price = self.calculate_total_price(pricing)
            return Response({"total_price": total_price}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calculate_total_price(self, pricing):
        # Implement your dynamic pricing calculation logic here
        # You can use the pricing fields like base_distance, base_price, per_km_price, etc.
        total_price = pricing.base_price  # Example calculation
        return total_price
