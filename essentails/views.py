# from django.views.decorators.csrf import csrf_exempt

from essentails import serializers
from essentails.models import Brand, Form, Item, User, UserItem
from essentails.serializers import BrandSerializer, FormSerializer, ItemSerializer, UserItemInfoSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

def index(request):
    return HttpResponse('Hello world')

class FormList(APIView):

    def get(self, request, format=None):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FormSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormDetail(APIView):

    def get_object(self, pk):
        try:
            form = Form.objects.get(pk=pk)
            return form
        except Form.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        form = self.get_object(pk)
        serializer = FormSerializer(form)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        form = self.get_object(pk)
        serializer = FormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        form = self.get_object(pk)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BrandList(APIView):

    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(APIView):

    def get_object(self, pk):
        try:
            brand = Brand.objects.get(pk=pk)
            return brand
        except Brand.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        brand = self.get_object(pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemList(APIView):
    
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):

    def get_object(self, pk):
        try:
            item = Item.objects.get(pk=pk)
            return item
        except Item.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        item = self.get_object(pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get_data(self, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_data(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserItemInfoList(APIView):

    def get(self, request, format=None):
        useriteminfo = UserItem.objects.all()
        serializer = UserItemInfoSerializer(useriteminfo, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserItemInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)