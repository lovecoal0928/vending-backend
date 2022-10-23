from rest_framework import generics
from rest_framework.permissions import AllowAny
from vending.models import Drinks
from vending.serializers import DrinksSerializer

class DrinksView(generics.ListAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    permission_classes = (AllowAny,)