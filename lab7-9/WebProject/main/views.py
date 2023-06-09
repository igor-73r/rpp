from django.shortcuts import render, redirect
from .models import *
from .forms import TotalForm


def index(request, table=Total):
    fields_name = [f.name for f in table._meta.fields]
    table_name = table.__name__
    query_results = table.objects.all()
    return render(request, 'main\index.html', locals())


def edit(request, id):
    instance = Total.objects.get(id=id)
    if request.method == 'POST':
        form = TotalForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TotalForm(instance=instance)
    context = {'form': form}
    return render(request, 'main/edit.html', context)


def add_new(request):
    if request.method == 'POST':
        form = TotalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TotalForm()
    context = {'form': form}
    return render(request, 'main/edit.html', context)


def remove(request, id):
    if request.method == 'POST':
        instance = Total.objects.get(id=id)
        instance.delete()
        return redirect('/')

def change_table(request):
    if 'Area' in request.POST:
        return index(request, Area)
    elif "Pos" in request.POST:
        return index(request, Position)
    elif "Type" in request.POST:
        return index(request, PrecipitationType)
    elif "Prec" in request.POST:
        return index(request, Precipitation)
    else:
        return index(request, Total)
