

salario = float(input("\nInsira seu salario: R$ \n"))

despesas = []

while True:

    descricao = input("Qual é a sua despesa?: ")
    valor = float(input("Insira o valor da sua despesa: R$ "))

    despesas.append([descricao, valor])

    continuar = input("Deseja continuar? [Sim/Não]: ")
    if continuar == "Não":
        break

total_gastos = 0

for despesa in despesas:
    total_gastos += despesa[1]

saldo = salario - total_gastos

print("\n RESUMO FINANCEIRO\n")

for despesa in despesas:
    print(f"{despesa[0]}: R$ {despesa[1]}")

print(f"\nTotal gasto: R$ {total_gastos}\n")
print(f"Saldo restante: R$ {saldo}")







