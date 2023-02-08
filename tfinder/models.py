from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class destination(models.Model):
	"""docstring for ClassName"""
	SUB_CHOICES= [
	('Maths', 'Maths'),
	('Physics', 'Physics'),
	('Chemistry', 'Chemistry'),
	('Programming', 'Programming'),
	('Other', 'Other'),]
	gen=[
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other'),
	]
	level= [
	('Grade', 'Grade'),
	('Secondary', 'Secondary'),
	('Intermediate', 'Intermediate'),
	('B.Tech', 'B.Tech'),
	('Other', 'Other'),]	
	desig= [
	('Teacher', 'Teacher'),
	('Lecturer', 'Lecturer'),
	('Asst Prof', 'Asst Professor'),
	('Assoc Prof', 'Assoc Professor '),
	('Professor ', 'Professor '),
	('Other', 'Other'),]
	user = models.ForeignKey(User,null = True,on_delete = models.CASCADE)	
	name = models.CharField(verbose_name="Name",max_length =100)
	phno  = models.CharField(verbose_name="Ph.No",max_length =10)
	email = models.EmailField(verbose_name="Email id",max_length=254)
	des  = models.CharField(verbose_name="Designation",choices=desig,max_length =20)
	age = models.IntegerField(verbose_name="Age")
	gender = models.CharField(verbose_name="Gender",choices=gen,max_length =20)
	sub= models.CharField(verbose_name="Expect Subject",choices=SUB_CHOICES,max_length =20)
	lev= models.CharField(verbose_name="Highest Level",choices=level,max_length =20)
	exp= models.IntegerField(verbose_name="Experience")
	loc  = models.CharField(verbose_name="Location",max_length =100)
	desp = models.TextField(verbose_name="Description",)


class posted(models.Model):
	gen=[
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other'),
	('Any', 'Any'),
	]
	s = [
	('Open','Open'),
	('Closed','Closed')
	]
	user = models.ForeignKey(User,null = True,on_delete = models.CASCADE)
	phno  = models.CharField(verbose_name="Ph.No",max_length =10)
	email = models.EmailField(verbose_name="Email id",max_length=254)
	des  = models.CharField(verbose_name="Designation",max_length =100)
	gender = models.CharField(verbose_name="Gender",choices=gen,max_length =20)
	sub= models.CharField(verbose_name="Expect Subject",max_length =20)
	exp= models.IntegerField(verbose_name="Experience")
	loc  = models.CharField(verbose_name="Location",max_length =100)
	desp = models.TextField(verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True)