'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


'''

from exerc_pacote_moeda_ver1.utilidades import moeda
from exerc_pacote_moeda_ver1.utilidades import dado

# se fosse um pacote seria: from exerc_modulo_moeda import moeda

p = float(input('Digite o preço R$: '))
moeda.resumo(p, 20, 12)