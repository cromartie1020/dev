from django.shortcuts import render
import random

def home(request):
    return render(request,'passwords/home.html')


def password(request):
    
    characters=list('abcdefghijklmnopqrstuvwxyz')
    

    password=''
    
    length=request.GET['length']
    length=int(length)
    if (request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if (request.GET.get('numbers')):
        characters.extend(list('0123456789'))

    if (request.GET.get('specials')):
        characters.extend(list('~!@#$%^&*()+-'))
    

    for x in  range(length):
        password+=random.choice(characters)
    
    
    return render(request,'passwords/password.html',{'password':password})

def about(request):
    return render(request,'passwords/about.html')
