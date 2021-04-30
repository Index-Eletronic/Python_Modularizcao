'''
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''

from exerc_pacote_moeda_ver2.utilidades import moeda
from exerc_pacote_moeda_ver2.utilidades import dado

# se fosse um pacote seria: from exerc_modulo_moeda import moeda

p = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(p, 20, 12)