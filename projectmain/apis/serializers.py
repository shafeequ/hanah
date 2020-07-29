from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'url', 'service_email', 'service_phone', 'image', 'terms', 'bill_country',
                  'country_of_residence', 'activation_date']
        depth = 1

    def create(self, validated_data):
        """Either create a new record or update existing base don the id field, do not create duplicate records"""
        vendor, _ = Vendor.objects.get_or_create(**validated_data)
        return vendor
