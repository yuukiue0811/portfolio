from django.shortcuts import render, redirect
from .models import BoycostsModel, GirlscostsModel, ShoppingcostsModel, ProfitModel
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def BoysList(request):
    model = BoycostsModel.objects.all().order_by("-date")

    obj = BoycostsModel.objects.filter(pk__gte=1)
    constant = 0
    for item in obj:
        constant += item.salary
        item.salary_total = constant
    return render(request, 'boys_list.html', {'model' : model, 'obj' : obj})

class BoysCreate(CreateView):
    template_name = 'boys_create.html'
    model = BoycostsModel
    fields = ('name', 'hour', 'wage', 'fixedsalary', 'allowance', 'mounth_allowance')
    success_url = reverse_lazy('boys_list')

class BoysDelete(DeleteView):
    template_name = 'boys_delete.html'
    model = BoycostsModel
    success_url = reverse_lazy('boys_list')

class BoysUpdate(UpdateView):
    template_name = 'boys_update.html'
    model = BoycostsModel
    fields = ('name', 'hour', 'wage', 'fixedsalary', 'allowance', 'mounth_allowance')
    success_url = reverse_lazy('boys_list')

def boys_detail(request, pk):
    object = BoycostsModel.objects.get(pk=pk)
    return render(request, 'boys_detail.html', {'object' : object })

def boys_salary(request, pk):
    object = BoycostsModel.objects.get(pk=pk)
    object.salary = object.wage * object.hour + object.allowance + object.mounth_allowance + object.fixedsalary
    object.save()
    return redirect('boys_list')

@login_required(login_url='/login/')
def GirlsList(request):
    model = GirlscostsModel.objects.all().order_by("-date")

    obj = GirlscostsModel.objects.filter(pk__gte=1)
    constant = 0
    for item in obj:
        constant += item.salary
        item.salary_total = constant
    return render(request, 'girls_list.html', {'model' : model, 'obj' : obj})

class GirlsCreate(CreateView):
    template_name = 'girls_create.html'
    model = GirlscostsModel
    fields = ('name', 'hour', 'wage', 'drinkbag', 'drinkbag_count', 'drinkbag_in', 'drinkbagin_count', 'bag', 'champagne_bag')
    success_url = reverse_lazy('girls_list')

class GirlsDelete(DeleteView):
    template_name = 'girls_delete.html'
    model = GirlscostsModel
    success_url = reverse_lazy('girls_list')

class GirlsUpdate(UpdateView):
    template_name = 'girls_update.html'
    model = GirlscostsModel
    fields = ('name', 'hour', 'wage', 'drinkbag', 'drinkbag_count', 'drinkbag_in', 'drinkbagin_count', 'bag', 'champagne_bag')
    success_url = reverse_lazy('girls_list')

def girls_detail(request, pk):
    object = GirlscostsModel.objects.get(pk=pk)
    return render(request, 'girls_detail.html', {'object' : object })

def girls_salary(request, pk):
    object = GirlscostsModel.objects.get(pk=pk)
    object.salary = object.wage * object.hour + object.drinkbag * object.drinkbag_count + object.drinkbag_in
    + object.drinkbagin_count + object.bag + object.champagne_bag
    object.save()
    return redirect('girls_list')

@login_required(login_url='/login/')
def ShoppingList(request):
    model = ShoppingcostsModel.objects.all().order_by("-date")

    obj = ShoppingcostsModel.objects.filter(pk__gte=1)
    constant = 0
    for item in obj:
        constant += item.shopping_total
        item.shopping_total = constant
    return render(request, 'shopping_list.html', {'model' : model, 'obj' : obj})

class ShoppingCreate(CreateView):
    template_name = 'shopping_create.html'
    model = ShoppingcostsModel
    fields = ('shopping_costs', 'others', 'profit')
    success_url = reverse_lazy('shopping_list')

class ShoppingDelete(DeleteView):
    template_name = 'shopping_delete.html'
    model = ShoppingcostsModel
    success_url = reverse_lazy('shopping_list')

class ShoppingUpdate(UpdateView): 
    template_name = 'shopping_update.html'
    model = ShoppingcostsModel
    fields = ('shopping_costs', 'others', 'profit')
    success_url = reverse_lazy('shopping_list')

def shopping_detail(request, pk):
    object = ShoppingcostsModel.objects.get(pk=pk)
    return render(request, 'shopping_detail.html', {'object' : object })

def shopping_costs(request, pk):
    object = ShoppingcostsModel.objects.get(pk=pk)
    object.shopping_total = object.shopping_costs + object.others - object.profit
    object.save()
    return redirect('shopping_list')

def profit(request):
    obj = ProfitModel.objects.all()
    return render(request, 'profit.html', {'obj' : obj })

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('home')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
      
        else:
            return render(request, 'login.html', {'context': 'usernameかpasswordが間違っています'})
    return render(request, 'login.html')


def logoutfunc(request):
    logout(request)
    return redirect('home')
