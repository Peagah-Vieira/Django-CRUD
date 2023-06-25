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
    vnome = request.POST.get("name")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)


def edit(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})
