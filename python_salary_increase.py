import IPython.display
from IPython.display import clear_output as clear
import time

#Calcula aumento do salário
def aumento(salario, porcentagem):
  porcentagem=porcentagem/100
  salario=(salario*porcentagem)+salario
  return salario

print("Calculadora de aumento de salário \n")
time.sleep(3)
clear()

#Coleta de valores
salario=float(input("Qual o seu salário atual? \n"))
porcentagem=float(input("Quanto você recebeu de aumento? (Valor em porcentagem sem o sinal de %) \n"))
clear()

#conversão para separação decimal Brasileira
salarioNovo=aumento(salario,porcentagem)
salarioNovo=f'{salarioNovo:_.2f}'
salarioNovo=salarioNovo.replace('.',',')
salarioNovo=salarioNovo.replace('_','.')

salario=f'{salario:_.2f}'
salario=salario.replace('.',',')
salario=salario.replace('_','.')

porcentagem=f'{porcentagem:_.2f}'
porcentagem=porcentagem.replace('.',',')
porcentagem=porcentagem.replace('_','.')

#Retorno de Resultado
print(f'Seu salário anterior era de: R${salario}')
print(f'Com um aumento de: {porcentagem}% \n')
print(f'Seu novo salário fica de: \nR${salarioNovo}')