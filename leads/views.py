from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.


def lead_list(request):
    lead = Lead.objects.all()
    context = {
        "leads": lead
    }
    return render(request, "leads/lead_list.html", context)


# pk stands for primary key
def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    return HttpResponse(lead)
