menu = """
----MENU----
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair
------------

Escolha a opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu.lower())

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0.1:
            saldo += valor_deposito
            extrato += f"Depósito no valor R$ {valor_deposito:.2f}\n"
            print(f"Seu depósito no valor de R$ {valor_deposito:.2f} foi realizado!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    if opcao == "s":
        valor_saque = float(input("Qual o valor que deseja sacar: R$ "))
        if valor_saque > saldo or limite_saques == 0:
            print("Saque indisponível, entre em contato com sua gerente.")
        else:
            saldo -= valor_saque
            extrato += f"Saque no valor de R$ {valor_saque:.2f}\n"
            print(f"Seu saque no valor de R$ {valor_saque:.2f} foi realizado!")
            limite_saques -= 1
            
    
    if opcao == "e":
        print(f"Sua movimentação:\n{extrato}")
        print("----------------------------------------------")
        print(f"Operações de saque permitidas: {limite_saques}")
        print("----------------------------------------------")
        print(f"O seu limite de saques é de R$ {limite}.")

    
    if opcao == "q":
        print("Operação Finalizada!")
        break

