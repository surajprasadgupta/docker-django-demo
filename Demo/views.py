from django.shortcuts import render
from rest_framework import serializers
from Demo.serializers import PersonSerializer,EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Demo.models import *

# Create your views here.



#------------------------------------Person CRUD Operations---------------------------------
class PersonListView(APIView):
    """
    List all Person, or create a new Person.
    """
    def get(self, request, format=None):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data,status=200)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Person.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   



         


class PersonDetailView(APIView):
    """
    Retrieve, update or delete a Person instance.
    """
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Person = self.get_object(pk)
        serializer = PersonSerializer(Person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Person = self.get_object(pk)
        serializer = PersonSerializer(Person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Person = self.get_object(pk)
        Person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        




#------------------------------------Employee CRUD Operations---------------------------------


class EmployeeListView(APIView):
    """
    List all Employee, or create a new Person.
    """
    def get(self, request, format=None):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data,status=200)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Employee.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeDetailView(APIView):
    """
    Retrieve, update or delete a Employee instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Employee = self.get_object(pk)
        Employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)