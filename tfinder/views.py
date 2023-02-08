from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import destination,posted
from django.contrib.auth.models import User ,auth
from .filters import desFilter,postFilter
from .forms import tegisterForm,postForm
from django.contrib import messages
from datetime import date
# Create your views here.
def index (request):
	return render(request,'index.html')

def home (request):
	dest,r = 0,0
	k = request.user.first_name
	if k == 'tutor':
		r=1
	if destination.objects.filter(user_id = request.user.id).exists():
		dest = 1
	context  = {'dest':dest,'r':r}
	return render(request,'home.html',context)

def locator (request):
	dest = destination.objects.all()
	myFilter = desFilter(request.GET, queryset=dest)
	dest = myFilter.qs
	final = {'dest':dest,'myFilter':myFilter}
	return render(request,'locator.html', final)

def register(request):
	if request.method == "POST":
		user_name = request.POST['user_name']
		role =  request.POST['role']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if password1 == password2:
			try:
				user = User.objects.create_user(username = user_name,password = password1,email = email,first_name = role)
				user.save()
				return redirect('login')
			except Exception as e:
				messages.error(request, 'Please Change the UserName..!')
				return redirect('register')		
			
		else:
			messages.error(request, 'Please Check password..!')
			return redirect('register')


	else:
		return render(request,'register.html')

def login(request):
	if request.method == "POST":
		username = request.POST['user_name']
		password = request.POST['password']
		user =auth.authenticate(username = username,password = password)

		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.error(request, 'Please Check the credentials!')
			return redirect('login')

	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('index')

def tregister(request):
	form = tegisterForm()
	user = request.user
	if request.method == 'POST':
		form = tegisterForm(request.POST)
		if form.is_valid():
			r = form.save(commit=False)
			r.user = User.objects.get(username=request.user)
			r.save()
			return redirect('home')
		else:
			messages.error(request, 'Please Check the data!')
	
	return render(request,'tregister.html',{'form':form})

def updatedata(request):
	dest = destination.objects.filter(user_id = request.user.id).first()
	form = tegisterForm(instance=dest)
	if request.method == 'POST':
		form = tegisterForm(request.POST, instance=dest)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context = {'form':form,'dest':dest}
	return render(request,'tregister.html',context)

def post(request):
	form = postForm()
	user = request.user
	if request.method == 'POST':
		form = postForm(request.POST)
		if form.is_valid():
			r = form.save(commit=False)
			r.user = User.objects.get(username=request.user)
			r.save()
			return redirect('home')
		else:
			messages.error(request, 'Please Check the data!')
	return render(request,'post.html',{'form':form})

def postv (request):
	r=0
	k = request.user.first_name
	if k == 'tutor':
		today = date.today()
		dest = posted.objects.all()
		dest =dest.filter(created_at__year=today.year,created_at__month=today.month)
		final = {'dest':dest}
		return render(request,'postv.html', final)
	else:
		r = 1
		dest = posted.objects.filter(user_id = request.user.id)
		final = {'dest':dest,'r':r}
		return render(request,'postv.html',final)
