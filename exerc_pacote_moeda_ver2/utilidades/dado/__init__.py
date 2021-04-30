def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha(): #Se a entrada for alfanumerico.
            print(f'ERRO: \"{entrada}"\ é um preço invalido')
        else:
            valido = True
            return float(entrada)