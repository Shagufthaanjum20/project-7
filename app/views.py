from django.shortcuts import render

# Create your views here.
def newpage(request):
    return render(request,'newpage.html')