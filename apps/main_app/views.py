from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import math
import random
from random import choice

def randInt(min=0, max=100):
    max-=min
    num = random.random() * max + min
    return num
datetime = strftime("%Y-%m-%d %H:%M %p",  gmtime())

def casino1():
    num = (math.floor(randInt(min=0, max=51)))
    return num
def casino2():
    num = (math.floor(randInt(min=-50, max=0)))
    return num
options = [casino1, casino2]


def index(request):

    request.session['num'] = 0
    if 'gold' in request.session:
        request.session['gold'] = request.session['gold']
    else:
        request.session['gold'] = 0
    if 'activity' in request.session:
        request.session['activity'] = request.session['activity']
    else:
        request.session['activity'] = []
    if 'counter' in request.session:
        request.session['counter'] = request.session['counter']
    else:
        request.session['counter'] = 1
    if 'condition1' in request.session:
        request.session['condition1'] = request.session['condition1']
    else:
        request.session['condition1'] = 100
    if 'condition2' in request.session:
        request.session['condition2'] = request.session['condition2']
    else:
        request.session['condition2'] = 10
    if 'goldamount' in request.session:
        request.session['goldamount'] = request.session['goldamount']
    else:
        request.session['goldamount'] = 100
    if 'totalturns' in request.session:
        request.session['totalturns'] = request.session['totalturns']
    else:
        request.session['totalturns'] = 10
    return render(request,'main_app/index.html')
    

def process(request):
    if request.method == "POST":
        if int(request.session['gold']) >= int(request.session['condition1']) and int(request.session['counter']) <= int(request.session['condition2']):
            print('you win!')
            return redirect('/victory')
        if int(request.session['gold']) < int(request.session['condition1']) and int(request.session['counter']) == int(request.session['condition2']):
            print('you lose!')
            return redirect('/loss')

        if request.POST['which_form'] == 'farm':
            request.session['num'] = math.floor(randInt(min=10, max=21))
            request.session['gold'] += request.session['num']
            request.session['activity'].insert(0, f"Earned {request.session['num']} from the farm! ({ datetime })")
            request.session['counter'] += 1
            print(request.session['activity'])
        if request.POST['which_form'] == 'cave':
            request.session['num'] = math.floor(randInt(min=5, max=11))
            request.session['gold'] += request.session['num']
            request.session['activity'].insert(0, f"Earned {request.session['num']} from the cave! ({ datetime })")
            request.session['counter'] += 1
            print(request.session['activity'])
        if request.POST['which_form'] == 'house':
            request.session['num'] = math.floor(randInt(min=2, max=6))
            request.session['gold'] += request.session['num']
            request.session['activity'].insert(0, f"Earned {request.session['num']} from the house! ({ datetime })")
            request.session['counter'] += 1
            print(request.session['activity'])
        if request.POST['which_form'] == 'casino':
            request.session['num'] = choice(options)()
            request.session['gold'] += request.session['num']
            if request.session['num'] >= 0:
                request.session['activity'].insert(0, f"Earned {request.session['num']} from the casino! ({ datetime })")
            else:
                request.session['activity'].insert(0, f"Lost {request.session['num']} from the casino... Ouch! ({ datetime })")
            print(request.session['activity'])
            request.session['counter'] += 1
    return redirect('/')



def reset(request):
    request.session.pop('gold')
    request.session.pop('activity')
    request.session.pop('num')
    request.session.pop('counter')
    # request.session.clear()
    request.session['condition1'] = request.session['goldamount']
    request.session['condition2'] = request.session['totalturns']
    return redirect('/')

def fullreset(request):
    request.session.clear()
    return redirect('/')