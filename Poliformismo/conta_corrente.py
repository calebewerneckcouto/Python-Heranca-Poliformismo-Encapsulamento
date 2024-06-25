from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, saldo_inicial=0.0, taxa_manutencao=10.0, limite_cheque_especial=0.0):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque_especial = limite_cheque_especial
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo + self.limite_cheque_especial >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser maior que zero.")
    
    def resumo(self):
        super().resumo()
        print(f"Tipo: Conta Corrente")
        print(f"Limite de Cheque Especial: R${self.limite_cheque_especial:.2f}")
        print(f"Taxa de Manutenção: R${self.taxa_manutencao:.2f}")
        print("-" * 20)
