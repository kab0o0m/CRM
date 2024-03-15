from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForm
# Create your views here.


def lead_list(request):
    lead = Lead.objects.all()
    context = {
        "leads": lead
    }
    return render(request, "leads/lead_list.html", context)


# pk stands for primary key
def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }

    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": LeadModelForm()
    }
    return render(request, "leads/lead_create.html", context)
