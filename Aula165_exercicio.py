# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

# def mes_pagamento(data):
#     parcela = 1
#     print(data_pagamento, valor_parcela)
#     parcela += 1

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
parcelas = relativedelta(years=5)
data_final = data_emprestimo + parcelas

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas
i = 1
for data in data_parcelas:
    data = data.strftime('%d/%m/%Y')
    print(f'Parcela: {i} \nData: {data} \nValor: R$ {valor_parcela:,.2f}\n')
    # valor_parcela = (valor_parcela * 1.01)
    i += 1
