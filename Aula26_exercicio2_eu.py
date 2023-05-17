"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario_input = int(input('Que horas são agora? '))



if (horario_input >= 0) and (horario_input <= 11):
    print('Bom dia.')
elif (horario_input >= 12) and (horario_input <= 17):
    print('Boa tarde.')
elif (horario_input >= 18) and (horario_input <= 23):
    print('Boa noite.')
else:
    print('Digite um horário válido')

