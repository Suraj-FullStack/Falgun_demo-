from django.shortcuts import render
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItem, category, Table  
from .serializers import categorySerializer, TableSerializer 
from rest_framework.serializers import ValidationError
from rest_framework import status
    # Create your views here.
#class based views
from rest_framework.views import APIView
from rest_framework import generics, mixins
class categoryGenericview(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = category.objects.all()
    serializer_class = categorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class categoryDetailGenericview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = category.objects.all()
    serializer_class = categorySerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)

class tableGenericview(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
# class CategoryList(APIView):
#     def get(self, request):
#         categories = category.objects.all()
#         serializer = categorySerializer(categories, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = categorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CategoryDetail(APIView):
#     def get(self, request, id):
#         cat = category.objects.get(id=id)
#         serializer = categorySerializer(cat)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def delete(self, request, id):
#         category = category.objects.get(id=id)
#         category.delete()
#         return Response({"Details": "Data has been deleted "}, status=status.HTTP_200_OK)
     
#     def update(self, request, id):
#         category = category.objects.get(id=id)
#         serializer = categorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TableList(APIView):
#     def get(self, request):
#         tables = Table.objects.all()
#         serializer = TableSerializer(tables, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TableDetail(APIView):
#     def get(self, request, id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def delete(self, request, id):
#         table = Table.objects.get(id=id)
#         table.delete()
#         return Response({"Details": "Table has been deleted "}, status=status.HTTP_200_OK)
     
#     def put(self, request, id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Function based view 
# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = category.objects.all()
#         serializer = categorySerializer(categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = categorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
      

# @api_view(['GET', 'DELETE'])
# def category_details(request, id):
#     if request.method == 'GET':
#         cat = category.objects.get(id=id)
#         serializer = categorySerializer(cat)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#      item =  OrderItem.objects.filter(menu__category = category).count()
#     if item > 0:
#       raise ValidationError({"Details": "This category cannot be deleted because it is associated with existing menu items."})
         
#     category.delete()  
#     return Response({"Details": "Data has been deleted "})


