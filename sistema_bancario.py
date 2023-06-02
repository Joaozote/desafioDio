menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """

saldo = 0
VALOR_LIMITE_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite a quantidade que deseja depositar: "))
        if valor_deposito <= 0:
            print("Por favor digite um valor válido!")
        else:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print("Deposito realizado com sucesso")
    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        saldo_excedido = valor_saque > saldo
        limite_excedido = valor_saque > VALOR_LIMITE_SAQUE
        saques_diarios_excedidos = numero_saques >= LIMITE_SAQUES
        
        if saldo_excedido:
            print("Você não tem essa quantia para sacar!")
        elif limite_excedido:
            print("Você só pode sacar R$500 por dia!")
        elif saques_diarios_excedidos:
            print("Você já realizou o limite de saques diários!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque: .2f}"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações!")
        else:
            print(extrato + f"\n Saldo da conta: {saldo: .2f}")
    elif opcao == "q":    
        break
    else:
        print("Operação inválida. Por favor selecione uma nova operação válida!")