from rest_framework import serializers
from .models import CustomerDetails

class CustomerSerialization(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerDetails
        fields = '__all__'