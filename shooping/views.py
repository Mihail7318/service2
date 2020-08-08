from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from datetime import datetime

from .serializers import CityListSerializer, StreetListSerializer, ShopCreateSerializer, ShopSerializer
from .models import City, Street, Shoop

class CityListView(APIView):
    def get(self, request):
        citys = City.objects.all()
        serializer = CityListSerializer(citys, many=True)
        return Response(serializer.data)

class StreetListView(APIView):
    def get(self, request):
        streets = Street.objects.all()
        serializer = StreetListSerializer(streets, many=True)
        return Response(serializer.data)


class ShopCreateView(APIView):
    def post(self, request):
        shop = ShopCreateSerializer(data=request.data)
        if shop.is_valid():
            shop.save()
        return Response(shop.data)

class ShopView(APIView):
    def get(self, request):
        street = request.GET.get("street", "all")
        city = request.GET.get("city","all")
        open = request.GET.get("open","all")
        q = Q()
        if street != 'all':
            q &= Q(street__name__exact=street)
        if city != 'all':
            q &= Q(city__title__exact=city)
        if open != 'all':
            time = datetime.now()
            if(open == "1"):
                q &= Q(open_time__lt=time, close_time__gt=time)
            if(open == "0"):
                q &= Q(open_time__lt=time, close_time__lt=time)

        shop = Shoop.objects.filter(q)

        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data)
