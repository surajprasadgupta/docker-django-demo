from django.test import TestCase
from Demo.models import Person,Employee

# Create your tests here.

class PersonModelTesting(TestCase):
	def setup(self):
		person=Person.objects.create(name="raj kumar",email="raj@gmail.com",age=45,phone="8896337174",address="noida india")
		return person
	def test_post_model(self):
		per=self.setup()
		self.assertTrue(isinstance(per,Person))
		self.assertEqual(str(per), 'raj kumar')
		
	def test_get_model(self):
		pass
	def test_put_model(self):	
		pass 
	def test_delete_model(self):	
		pass	

class EmployeeModelTesting(TestCase):
	def setup(self):
		person=Person.objects.create(name="raj kumar",email="raj@gmail.com",age=45,phone="8896337174",address="noida india")
		line_manager=Person.objects.create(name="suraj gupta",email="raj@gmail.com",age=45,phone="8896337174",address="noida india")
		employee=Employee.objects.create(person_id=person,department="IT",role="developer",line_manager=line_manager)
		return employee

	def test_post_model(self):
		emp=self.setup()
		self.assertTrue(isinstance(emp,Employee))
		self.assertEqual(str(emp), 'raj kumar')		

	def test_get_model(self):
		pass
	def test_put_model(self):	
		pass 
	def test_delete_model(self):	
		pass