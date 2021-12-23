from django.db import models

# Create your models here.

# Person (name, email, age, phone, address, created datetime, modified datetime)
# Employee (person_id Foreign Key, department, role, line_manager person_id Foreign Key, created datetime, modified datetime)

class Person(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	age=models.IntegerField()
	phone=models.CharField(max_length=12)
	address=models.CharField(max_length=100)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Employee(models.Model):
	person_id=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='Employee')
	department=models.CharField(max_length=100)
	role=models.CharField(max_length=50)
	line_manager=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='Person')
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.person_id.name


