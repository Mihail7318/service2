from rest_framework import serializers
from .models import City, Street, Shoop


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"

class StreetListSerializer(serializers.ModelSerializer):
    #city = serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = Street
        fields = "__all__"

class ShopCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoop
        fields = "__all__"

    def create(self, validated_data):
        return Shoop.objects.create(**validated_data)

class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field="title", read_only=True)
    street = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Shoop
        fields = "__all__"