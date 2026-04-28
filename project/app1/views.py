from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItem, category, Table  
from .serializers import categorySerializer, TableSerializer  
# Create your views here.
@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        categories = category.objects.all()
        serializer = categorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'DELETE'])
def category_list(request,id):
    if request.method == 'GET':
        category = category.objects.get(id=id)
        serializer = categorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'DELETE':
      category = category.objects.get(id=id)
      Items = OrderItem.objects.filter(menu__category= category).count()
      if Items > 0:
          return Response({'error': 'Cannot delete category with associated menu items.'}, status=400)
      category.delete()
    return Response(status=204)


@api_view(['GET', 'PUT'])
def table(request):
    if request.method == 'GET':
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)