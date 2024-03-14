from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.


def home_page(request):
    lead = Lead.objects.all()
    context = {
        "leads": lead
    }
    return render(request, "second_page.html", context)
