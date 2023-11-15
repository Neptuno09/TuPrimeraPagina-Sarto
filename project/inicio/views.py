from django.shortcuts import render

def inicio(request):
    return render(request,"inicio.html")
def success(request):
    return render(request,"success.html")