from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'victory/index.html')

def conditions(request):
    if request.method == "POST":
        request.session['goldamount'] = request.POST['goldamount']
        request.session['totalturns'] = request.POST['totalturns']
    return redirect('/reset')


