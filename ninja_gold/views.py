from django.shortcuts import render, redirect, HttpResponse
import random
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
        

    context = {
        'gold': request.session['gold'],
        
    }

    return render(request, 'index.html', context)

def ninjagold(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        # context = { "context" = request.session['counter´']
        return redirect(request,'index.html')


def login(request):
    #si llega un GET cargamos el formulario login.html
    if request.method == 'GET':
        
        return render(request,'login.html')
    #si llega un Post, logueamos y redireccionamos al casino
    else:
        print('Nombre: ', request.POST['nombre'])
        print('Pass: ', request.POST['password'])

        #guardamos el nombre del usuaria en session
        request.session['nombre'] = request.POST['nombre']

        #redirigimos
        return redirect('/')

def process_money(request,juego):
        request.session['activities'] = []
        gold = 0

        if juego == 'granja':
            rand = random.randint(10,20)

        elif juego == 'cueva':
            rand = random.randint(5,10)

        elif juego == 'casa':
            rand = random.randint(2,5)

        elif juego == 'casino':
            rand = random.randint(-50,50)

        #rand = random.randint(minim,maxim) calcula el numero aleatorio segun el rango
        
        request.session['gold'] += rand
        gold +=rand

        if gold >= 0:
            request.session['activities'].append({
                'text' : f'Haz ganado {gold} oros en {juego}',
                'golds' : request.session['gold']
            })
            request.session.save()

        else:
            request.session['activities'].append({
                'text' : f'Haz perdido {gold} oros en {juego}',
                'golds' : request.session['gold']
            })
            request.session.save()

        return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    
    return redirect('/')

