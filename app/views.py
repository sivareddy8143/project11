from django.shortcuts import render

# Create your views here
def samba(request):
    return render(request,'samba.html',context={'name':'samba','age':26})
