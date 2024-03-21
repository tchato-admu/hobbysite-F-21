from django.shortcuts import render

from commissions.models import Commissions


def commissions_list(request):
    commissions_list = {"commissions_list": Commissions.objects.all()}
    return render(request, "commission/commissions_list.html", commissions_list)


def commissions_detail(request, pk):
    commissions_detail = {"commissions_detail": Commissions.objects.get(pk=pk)}
    return render(request, "commission/commissions_detail.html", commissions_detail)

