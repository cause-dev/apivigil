from django.shortcuts import render

# Create your views here.


def monitor_list(request):
    return render(request, "base.html")
