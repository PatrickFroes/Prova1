saldo = 0
deposito = ()
saque = ()
continuar = 1
escolha = ()

while continuar == 1:
    print("Digite 1 para consultar seu saldo.")
    print("Digite 2 para fazer um saque.")
    print("Digite 3 para fazer um depósito.")
    print("digite 4 para sair.")
    escolha = float(input("O que deseja fazer?"))
    if escolha == 1:
        print("Seu saldo é de:",saldo,"reais.")
    elif escolha == 2:
        saque = float(input("Quanto deseja sacar?"))
        if saque <= saldo:
            saldo = saldo-saque
            print("Seu novo saldo é:", saldo,"reais.")
        else:
            print("valor indisponivel.")
    elif escolha == 3:
        deposito = float(input("Quanto deseja depositar?"))
        saldo = saldo + deposito
        print("Seu novo saldo é:", saldo,"reais.")
    elif escolha == 4:
        print("Até a proxima, fechando o programa.")
        continuar = 0
    else:
        print("Digito inválido.")




