from django.shortcuts import render

# Create your views here.
def usdfilters(request):
    d={'data':'hai HOw are you where'}
    return render(request,'usdfilters.html',d)
