from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

# Criando uma conta corrente e realizando operações
conta_corrente = ContaCorrente("123-4", "João", 1000.0, 15.0, 500.0)
conta_corrente.depositar(500.0)
conta_corrente.sacar(1200.0)
conta_corrente.resumo()

# Criando uma conta poupança e realizando operações
conta_poupanca = ContaPoupanca("567-8", "Maria", 2000.0, 0.05)
conta_poupanca.depositar(1000.0)
conta_poupanca.aplicar_juros()
conta_poupanca.resumo()
