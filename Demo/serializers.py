from rest_framework import serializers
from Demo.models import *




class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ('id','name','email','age','phone','address','created_on','updated_on')
        fields = '__all__' 



class EmployeeSerializer(serializers.ModelSerializer):
	# person = PersonSerializer(many=True, read_only=True)

	class Meta:
		model = Employee
		fields = '__all__' 






class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = []

