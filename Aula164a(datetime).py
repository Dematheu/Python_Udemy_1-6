# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

# from pytz import timezone

# data_str_data = '1991/10-24 07:49:23'
# data_str_fmt = '%Y/%m-%d %H:%M:%S'

# O formato deve seguir os mesmos caracteres de separação (/, - ou 'espaço')
# que a data em si.

# data = datetime(1991, 10, 24, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)

data = datetime.now()
# gerar a data (numero) para base de dados (ex.: 1679402382)
print(data.timestamp())
print(datetime.fromtimestamp(1679402382))  # Ler a data da base de dados.
