from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, a, b):
    soma_1 = a + b
    return HttpResponse('<h2>A soma é {}</h2>'.format(soma_1))

def diferenca(request, a, b):
    diferenca_1 = a - b
    return HttpResponse('<h2>A diferenca é {}</h2>'.format(diferenca_1))

def divisao(request, a, b):
    divisao_1 = a / b
    return HttpResponse('<h2>A divisão é {}</h2>'.format(divisao_1))

def multiplicacao(request, a, b):
    multiplicacao_1 = a * b
    return HttpResponse('<h2>A multiplicação é {}</h2>'.format(multiplicacao_1))