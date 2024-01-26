from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def read_data(request):
    N1 = int(request.POST['txtnum1'])
    N2 = int(request.POST['txtnum2'])
    res = request.POST['operation']
    if res == "Add":
        ans = N1+N2
    elif res =="Sub":
        ans = N1 - N2
    elif res =="Multi":
        ans = N1*N2
    elif res == "Div":
        if N1 > N2:
            ans = N1 // N2
        else:
            return render(request,'index.html',{'Ans2':"Division Error: First Number is greater than Second Number",'NUM1':N1,'NUM2':N2})
    elif res == "Rem":
        ans = N1 % N2

    return render(request,'index.html',{'Ans':ans,'NUM1':N1,'NUM2':N2})


def operation_fun(request):
    return render(request,'index.html')
