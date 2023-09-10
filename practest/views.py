from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from practest.models import Person
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import ast
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

def record_list(request):
    records = Person.objects.all()
    hobby_arr = []
    print(records)
    for i in records:
        hobbyObj = ast.literal_eval(i.hobbies)
        for key, value in hobbyObj.items():
            if (value == 1):
                hobby_arr.append(key)
        i.hobbies = ",".join(hobby_arr)
    return render(request,'practest/table.html', {'records': records})



@csrf_exempt
def person_add(request):
    if request.method == 'POST':
        #TODO: handle validation
        person1 = Person()
        person1.name=request.POST.get('name')
        person1.email=request.POST.get('email')
        person1.phone = request.POST.get('phone')
        person1.address = request.POST.get('address')
        person1.gender = request.POST.get('gender')
        person1.hobbies = ast.literal_eval(request.POST.get('hobby'))
        person1.save()
    return JsonResponse({"success":True,"message":"Person Data Added successfully"})


@csrf_exempt
def person_update(request,id):
    # TODO: handle validation
    if request.method == 'POST':
        person1 = Person.objects.get(id=id)
        person1.name = request.POST.get('name')
        person1.email = request.POST.get('email')
        person1.phone = request.POST.get('phone')
        person1.address = request.POST.get('address')
        person1.gender = request.POST.get('gender')
        person1.hobbies = ast.literal_eval(request.POST.get('hobby'))
        person1.save()
    return JsonResponse({"success":True,"message":"Person Data Updated successfully"})

@csrf_exempt
def person_delete(request):
    # handle validation
    if request.method == 'POST':
        id = request.POST.get("rid")
        person = Person.objects.get(pk=id)
        print(person)
        person.delete()
        return JsonResponse({"success":True,'message': 'Record deleted Successfully'})
    else:
        return JsonResponse({'message': 'Record deleted Successfully'})

# @api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="practest/register.html", context={"register_form": form})


def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("practest")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="practest/login.html", context={"login_form":form})
# Create your views here.
