menu = """Escolha uma das operações que deseja realizar:
[1] Depositar
[2] Sacar
[3] Exibir extrato
[0] Sair\n"""

NUM_SAQUE = 3
saldo = 0
limite_saque = 500
extrato = ""

print("Bem-vindo(a) ao banco DioBank!")

while True:

    opcao = int(input(menu))
    
    if opcao == 1:
        depositar = int(input("Digite o valor que deseja depositar: "))
        if depositar > 0:
            extrato += f"Depositou R${depositar}\n"
            saldo += depositar
        else:
            print("Digite um valor válido!")
    elif opcao == 2:       
        if NUM_SAQUE > 0:
            if saldo > 0:
                sacar = int(input("Digite o valor que deseja sacar: "))
                if sacar <= limite_saque and sacar <= saldo:
                    extrato += f"Sacou R${sacar}\n"
                    saldo -= sacar
                    NUM_SAQUE -= 1
                else:
                    print("Sem saldo para saque ou limite de R$500 ultrapassado.")
            else:
                print("Você não tem saldo para saque!")
        else:
            print("O Sr(a) atingiu o limite de saques diários!")
    elif opcao == 3:
        print(f"EXTRATO\n{extrato}\nSaldo final de R${saldo}")
        break
    elif opcao == 0:
        break
    else:
        print("Digite um valor válido!")

