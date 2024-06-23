from datetime import datetime

menu = """
[1] Cadastrar Usuário
[2] Cadastrar Conta Bancária
[3] Listar Contas Bancárias
[4] Encontrar Usuário por CPF
[5] Depósito
[6] Saque
[7] Extrato
[8] Sair

=>
"""

usuarios = []
contas_bancarias = []
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

def cadastrar_usuario():
    print("\n== Cadastro de Usuário ==")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")

    usuario = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

def cadastrar_conta_bancaria(usuario):
    print("\n== Cadastro de Conta Bancária ==")
    numero_conta = input("Número da conta: ")
    tipo_conta = input("Tipo de conta (Corrente/Poupança): ")
    saldo = float(input("Saldo inicial: "))

    conta = {
        'numero_conta': numero_conta,
        'tipo_conta': tipo_conta,
        'saldo': saldo,
        'usuario': usuario
    }

    contas_bancarias.append(conta)
    print("Conta bancária cadastrada com sucesso!")

def listar_contas():
    print("\n== Listagem de Contas Bancárias ==")
    if not contas_bancarias:
        print("Nenhuma conta bancária cadastrada.")
    else:
        for idx, conta in enumerate(contas_bancarias, start=1):
            print(f"\nConta {idx}:")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Tipo de Conta: {conta['tipo_conta']}")
            print(f"Saldo: R$ {conta['saldo']:.2f}")
            print(f"Titular: {conta['usuario']['nome']}")
            print(f"CPF: {conta['usuario']['cpf']}")
            print(f"Data de Nascimento: {conta['usuario']['data_nascimento']}")
    print("===============================")

def encontrar_usuario_por_cpf():
    cpf_procurado = input("Informe o CPF do usuário: ")
    encontrado = False

    for usuario in usuarios:
        if usuario['cpf'] == cpf_procurado:
            print("\n== Usuário Encontrado ==")
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            encontrado = True
            break
    
    if not encontrado:
        print("Usuário não encontrado.")

def realizar_deposito():
    print("\n== Depósito ==")
    numero_conta = input("Informe o número da conta: ")
    valor = float(input("Informe o valor de depósito: "))

    conta_encontrada = None
    for conta in contas_bancarias:
        if conta['numero_conta'] == numero_conta:
            conta['saldo'] += valor
            extrato = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
            return

    print("Conta não encontrada. Operação falhou!")

def realizar_saque():
    print("\n== Saque ==")
    numero_conta = input("Informe o número da conta: ")
    valor = float(input("Informe o valor de saque: "))

    conta_encontrada = None
    for conta in contas_bancarias:
        if conta['numero_conta'] == numero_conta:
            excedeu_saldo = valor > conta['saldo']
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                conta['saldo'] -= valor
                extrato = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
                return
            else:
                print("Operação falhou! O valor informado é inválido.")
                return

    print("Conta não encontrada. Operação falhou!")

def exibir_extrato():
    print("\n== Extrato ==")
    numero_conta = input("Informe o número da conta: ")

    for conta in contas_bancarias:
        if conta['numero_conta'] == numero_conta:
            print("============ EXTRATO ===========")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            print("===============================")
            return

    print("Conta não encontrada. Operação falhou!")

def main():
    while True:
        opcao = input(menu)
        
        if opcao == "1":
            cadastrar_usuario()
        
        elif opcao == "2":
            if not usuarios:
                print("Cadastre um usuário antes de criar uma conta bancária.")
            else:
                usuario = usuarios[-1]  # Pega o último usuário cadastrado
                cadastrar_conta_bancaria(usuario)
        
        elif opcao == "3":
            listar_contas()
        
        elif opcao == "4":
            encontrar_usuario_por_cpf()
        
        elif opcao == "5":
            realizar_deposito()
        
        elif opcao == "6":
            realizar_saque()
        
        elif opcao == "7":
            exibir_extrato()
        
        elif opcao == "8":
            break
        
        else:
            print("Opção inválida! Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
