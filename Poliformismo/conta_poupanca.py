from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular, saldo_inicial=0.0, taxa_juros=0.03):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.taxa_juros = taxa_juros
    
    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        print("Juros aplicados à conta poupança.")
    
    def resumo(self):
        super().resumo()
        print(f"Tipo: Conta Poupança")
        print(f"Taxa de Juros: {self.taxa_juros * 100}%")
        print("-" * 20)
