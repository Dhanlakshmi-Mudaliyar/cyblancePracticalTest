from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Person
from .forms import PersonForm
from django.views.decorators.csrf import csrf_exempt
import ast
def record_list(request):
    records = Person.objects.all()
    hobby_arr = []
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
        Person.objects.filter(id=id).delete()
        return JsonResponse({"success":True,'message': 'Record deleted Successfully'})
# Create your views here.
