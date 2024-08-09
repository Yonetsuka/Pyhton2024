#crie um aloritmo para calcular o descono de salário, bem como o salário
#a receber em função da porcentagem de desconto. Porém, utilize LISTAS e estrutura de entrada
# até 2.259,20 - isento
# 2.259,21 a 2.826,65 - 7,5%
# 2.826,66 a 3.751,05 - 15%
# 3.751,06 a 4.664,68 - 22,5%
# acima de 4.664,68 - 27,5%

lista_desconto = [
    (2259,0),
    (2828,0.075),
    (3571,0.15),
    (4664,0.225),
    (float('inf'),0.275)
]

salario_bruto = float(input("Digite seu salario: "))

for limite,percentual in lista_desconto:
    if salario_bruto <= limite:
        desconto = salario_bruto * percentual
        break
salario_receber = salario_bruto - desconto

print(f"Salario bruto: {salario_bruto}")
print(f"salario após o desconto: {salario_receber}")
