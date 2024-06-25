class Conta:
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser maior que zero.")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser maior que zero.")
    
    def resumo(self):
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo Atual: R${self.saldo:.2f}")
        print("-" * 20)
