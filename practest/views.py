from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from practest.models import Person
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import ast
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from .forms import NewUserForm
from practest.models import PractTestUsers
from django.contrib.auth.hashers import check_password,make_password
from django.core import serializers
import json
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
def person_delete(request,id):
    # handle validation
    if request.method == 'DELETE':
        person = Person.objects.get(pk=id)
        print(person)
        person.delete()
        return JsonResponse({"success":True,'message': 'Record deleted Successfully'})
    else:
        return JsonResponse({'message': 'Record deleted Successfully'})

# @api_view(['POST'])
@csrf_exempt
def register_user_api(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name","")
        last_name = request.POST.get("last_name","")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if not first_name or not last_name or not email or not password:
            return JsonResponse({"success":True,"message":"All fiedls are mandatory"})
        password = make_password(password)
        User = PractTestUsers.objects.filter(email=email).first()
        if(User):
            return JsonResponse({"success": False, "message": "User Already Registered"})
        p1 = PractTestUsers()
        p1.first_name = first_name
        p1.last_name = last_name
        p1.email = email
        p1.password = password
        p1.save()
        return JsonResponse({"success":True,"messages":"User Registered Successfully"})
    return render(request=request, template_name="practest/register.html")

@csrf_exempt
def register_user(request):
    return render(request=request, template_name="practest/register.html")

@csrf_exempt
def user_login_api(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if not email or not password:
            return JsonResponse({"success": True, "message": "All fiedls are mandatory"})
        User = PractTestUsers.objects.filter(email=email).first()
        if (not User):
            return JsonResponse({"success": False, "message": "User Not Registered"})
        if(not check_password(password, User.password)):
            return JsonResponse({"success": False, "message": "password not matched"})
        serialized_obj = serializers.serialize('json', [User])
        serialized_obj1 = json.loads(serialized_obj)
        return JsonResponse({"success": True, "message": "Login successFullly","User":serialized_obj1})
    return render(request=request, template_name="practest/login.html")

@csrf_exempt
def user_login(request):
    return render(request=request, template_name="practest/login.html")
# Create your views here.
