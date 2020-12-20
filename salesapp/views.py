from django.shortcuts import render, redirect
from .models import SalesModel
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class HomeClass(TemplateView):
    template_name = 'base.html'

@login_required(login_url='/login/')
def SaleList(request):
    model = SalesModel.objects.all().order_by("-date")

    obj = SalesModel.objects.filter(pk__gte=1)
    a = 0
    for item in obj:
        a += item.bill
        item.sales_total = a
    return render(request, 'list.html', {'model' : model, 'obj' : obj})


def detailfunc(request, pk):
    object = SalesModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object' : object })

d_price = 1000
d1_price = 0
tax = 1.1
def billfunc(request, pk):
    object = SalesModel.objects.get(pk=pk)
    if object.girlsdrink_confirmation == 'yes' and object.tax_confirmation == 'yes':
        object.bill = (object.tablecharge * object.custermer + object.girlsdrink_count * d_price
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge) * tax
        object.save()
        return redirect('list')
    elif object.girlsdrink_confirmation == 'yes' and object.tax_confirmation == 'no':
        object.bill = (object.tablecharge * object.custermer + object.girlsdrink_count * d_price 
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge)
        object.save()
        return redirect('list')
    elif object.girlsdrink_confirmation == 'no' and object.tax_confirmation == 'yes':
        object.bill = (object.tablecharge * object.custermer + object.girlsdrink_count * d1_price
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge) * tax
        object.save()
        return redirect('list')
    else:
        object.girlsdrink_confirmation == 'no' and object.tax_confirmation == 'no'
        object.bill = (object.tablecharge * object.custermer + object.girlsdrink_count * d1_price
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge)
        object.save()
        return redirect('list')

tax2 = 0.1
def taxfunc(request, pk):
    object = SalesModel.objects.get(pk=pk)
    if object.girlsdrink_confirmation == 'yes' and object.tax_confirmation == 'yes':
        object.tax_total = (object.tablecharge * object.custermer + object.girlsdrink_count * d_price 
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge) * tax2
        object.save()
        return redirect('list')
    elif object.girlsdrink_confirmation == 'yes' and object.tax_confirmation == 'no':
        object.tax_total = 0
        object.save()
        return redirect('list')
    elif object.girlsdrink_confirmation == 'no' and object.tax_confirmation == 'yes':
        object.tax_total = (object.tablecharge * object.custermer + object.girlsdrink_count * d1_price 
        + object.staff_reservation_fee + object.champagne_fee + object.singlecharge) * tax2
        object.save()
        return redirect('list')
    else:
        object.girlsdrink_confirmation == 'no' and object.tax_confirmation == 'no'
        object.tax_total = 0
        object.save()
        return redirect('list')


class SalesCreate(CreateView):
    template_name = 'create.html'
    model = SalesModel
    fields = ('tablenumber', 'girlsdrink_confirmation', 'tax_confirmation', 'singlecharge', 'tablecharge', 'custermer', 'girlsdrink_count', \
        'staff_reservation_fee', 'champagne_fee')
    success_url = reverse_lazy('list')

class SalesDelete(DeleteView):
    template_name = 'delete.html'
    model = SalesModel
    success_url = reverse_lazy('list')

class SalesUpdate(UpdateView):
    template_name = 'update.html'
    model = SalesModel
    fields = ('tablenumber', 'girlsdrink_confirmation', 'tax_confirmation', 'singlecharge', 'tablecharge', 'custermer', 'girlsdrink_count', \
        'staff_reservation_fee', 'champagne_fee')
    success_url = reverse_lazy('list')


