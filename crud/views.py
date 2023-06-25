from django.shortcuts import render, redirect
from .models import Pessoa


def home(request):
    people = Pessoa.objects.all()
    return render(request, "index.html", {"people": people})


def create(request):
    createName = request.POST.get("name")
    createLastName = request.POST.get("lastName")
    createEmail = request.POST.get("email")
    Pessoa.objects.create(
        name=createName, lastName=createLastName, email=createEmail)
    return redirect(home)


def update(request, id):
    updateName = request.POST.get("name")
    updateLastName = request.POST.get("lastName")
    updateEmail = request.POST.get("email")
    person = Pessoa.objects.get(id=id)
    person.name = updateName
    person.lastName = updateLastName
    person.email = updateEmail
    person.save()
    return redirect(home)


def delete(request, id):
    person = Pessoa.objects.get(id=id)
    person.delete()
    return redirect(home)


def edit(request, id):
    person = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"person": person})
