'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

'''


def aumentar(preco=0, taxa=0, formato=False):
    """

    :param preco:
    :param taxa:
    :param formato:
    :return:

    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco, moeda='R$'):
    return f'{moeda}{preco:2>.2f}'.replace('.', ',')  # Ira subistituir todos os pontos por virgula


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')  # -- \t é Tabulação. Para alinhar o texto.
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento : \t{aumentar(preco, taxar, True)}')
    print(f'{taxar}% de redução:  \t{diminuir(preco, taxar, True)}')
    print('-' * 30)