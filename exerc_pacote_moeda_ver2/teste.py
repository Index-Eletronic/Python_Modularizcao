'''
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''

from exerc_pacote_moeda_ver1.utilidades import moeda
from exerc_pacote_moeda_ver1.utilidades import dado

# se fosse um pacote seria: from exerc_modulo_moeda import moeda

p = float(input('Digite o preço R$: '))
moeda.resumo(p, 20, 12)