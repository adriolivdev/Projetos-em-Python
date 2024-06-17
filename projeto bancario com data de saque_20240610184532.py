from datetime import datetime

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":  # OPÇÃO DEPÓSITO...
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":  # OPÇÃO SAQUE...
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "3":  # OPÇÃO EXTRATO...
        print("============ EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    
    elif opcao == "4":  # OPÇÃO SAIR...
        break
    
    else:
        print("Opção inválida! Por favor, selecione novamente.")
