from commissions.models import Commission
from django.shortcuts import render


def commission_list(request):
    commission_list = {"commission_list": Commission.objects.all()}
    return render(request, "commission/commission_list.html", commission_list)


def commission_detail(request, pk):
    commission_detail = {"commission_detail": Commission.objects.get(pk=pk)}
    return render(request, "commission/commission_detail.html", commission_detail)

# Create your views here.
