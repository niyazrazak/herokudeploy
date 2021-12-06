from django.shortcuts import render

# Create your views here.

def indexFun(request):
    return render(request, index.html)
