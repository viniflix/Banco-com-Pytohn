from contas import *

Conta1 = ContaBancaria("Vinicius", 1, 200)
Conta2 = ContaBancaria("João", 2, 300)




menu = 0
while menu !=5:
    print('''Bem Vindo ao Branco!
o que deseja fazer?
[ 1 ] Depositar 
[ 2 ] Ver saldo
[ 3 ] Realizar saque
[ 4 ] Realizar tranferencia
[ 5 ] Sair''')
    menu = int(input("Digite aqui: "))

    if menu == 1:
        valor = int(input("Valor a depositar: "))
        Conta1.depositar(valor)
        
    elif menu == 2:
        Conta1.ver_saldo()
        
    elif menu == 3:
        saque = int(input("Valor a sacar: "))
        Conta1.sacar(saque)
        
    elif menu == 4:
        valor = int(input("Valor a transferir: "))
        Conta1.transferir(Conta2, valor)
        
    elif menu == 5:
        print('Finalizando...')
    else:
        print("Opção invalida, tente novamente!")
    print('=-=' * 10)
print("Fim do programa!")





