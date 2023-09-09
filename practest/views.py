from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Person
from .forms import PersonForm

def record_list(request):
    records = Person.objects.all()
    return render(request,'practest/record.html', {'records': records})



def person_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record')
    else:
        form = PersonForm()
    return render(request,'person/record_form.html',{'form':form})

def person_update(request,person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('record')

    else:
        form = PersonForm(instance=person)
    return render(request, 'person/person_update.html', {'form':form})


def person_delete(request,person_id):
    person = get_object_or_404(Person,id=person_id)
    if request.method == 'DELETE':
        person.delete()
        return JsonResponse({'message': 'Record deleted Successfully'})
# Create your views here.
