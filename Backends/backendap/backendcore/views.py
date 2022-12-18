from django.shortcuts import render,HttpResponse

def hello_django(request):
    return HttpResponse("hello Django")
