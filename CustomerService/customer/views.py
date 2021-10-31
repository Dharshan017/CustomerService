from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from .models import CustomerDetails
from .serializers import CustomerSerialization

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins

class GetPutDeleteAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerialization
    queryset = CustomerDetails.objects.all()

    lookup_field = 'id'
    
    def get(self,request,id=None):
        if id==None:
            return self.list(request)
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

class PostAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    serializer_class = CustomerSerialization
    queryset = CustomerDetails.objects.all()
    
    lookup_field = 'id'

    def get(self,request,id=None):
        if id==None:
            return self.list(request)
        return self.retrieve(request)


    def post(self,request):
        return self.create(request)