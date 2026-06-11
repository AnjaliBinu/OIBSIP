import random
from django.shortcuts import render

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    character = []
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('lowercase'):
        character.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))    
    if request.GET.get('symbols'):
        character.extend(list('!@#$%^&*()_+'))
        
    if not character:
        character.extend(list('abcdefghijklmnopqrstuvwxyz'))
        
    length = int(request.GET.get('length', 12))
    generated_password = ''
    for x in range(length):
        generated_password += random.choice(character)
        
    return render(request, 'generator/password.html', {'password': generated_password})