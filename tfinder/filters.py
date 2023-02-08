import django_filters
from django_filters import NumberFilter, CharFilter

from .models import *

class desFilter(django_filters.FilterSet):
	start_exp = NumberFilter(field_name="exp", lookup_expr='gte',label = "Minimum Experience ")
	start_age = NumberFilter(field_name="age", lookup_expr='gte',label = "Min Age")
	end_age = NumberFilter(field_name="age", lookup_expr='lte',label = "Max Age")
	desp = CharFilter(field_name='desp', lookup_expr='icontains',label = "Description")
	loc = CharFilter(field_name='loc', lookup_expr='icontains',label = "Desired Location ")
	class Meta:
		model = destination
		fields = '__all__'
		exclude  = ['name','phno','email','age','desp','exp','user']
class postFilter(django_filters.FilterSet):
	desp = CharFilter(field_name='desp', lookup_expr='icontains',label = "Description")
	loc = CharFilter(field_name='loc', lookup_expr='icontains',label = "Desired Location ")
	
	class Meta:
		model = posted
		fields = '__all__'
		exclude  = ['name','phno','email','age','desp','exp','user']

