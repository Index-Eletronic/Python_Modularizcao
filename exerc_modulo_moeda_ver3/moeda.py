'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(preco = 0, taxa = 0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco = 0, taxa = 0):
    res = preco - (preco * taxa /100)
    return res


def dobro(preco = 0):
    res = preco * 2
    return res


def metade(preco = 0):
    res = preco / 2
    return res

def moeda(preco, moeda= 'R$'):
    return f'{moeda}{preco:2>.2f}'.replace('.', ',') # Ira subistituir todos os pontos por virgula