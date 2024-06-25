class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

class Reserva:
    def __init__(self, cliente, quarto, num_diarias):
        self.cliente = cliente
        self.quarto = quarto
        self.num_diarias = num_diarias

class Hotel:
    def __init__(self, nome_hotel):
        self.nome_hotel = nome_hotel
        self.funcionarios = []
        self.reservas = []
        self.quartos_disponiveis = list(range(1, 101))  # Exemplo de 100 quartos numerados de 1 a 100

    def adicionar_funcionario(self, nome, funcao, salario):
        funcionario = Funcionario(nome, funcao, salario)
        self.funcionarios.append(funcionario)

    def fazer_reserva(self, cliente, num_quarto, num_diarias):
        if num_quarto in self.quartos_disponiveis:
            reserva = Reserva(cliente, num_quarto, num_diarias)
            self.reservas.append(reserva)
            self.quartos_disponiveis.remove(num_quarto)
            print(f"Reserva realizada para o quarto {num_quarto} por {num_diarias} diárias.")
        else:
            print(f"Quarto {num_quarto} não disponível.")

    def calcular_conta_final(self):
        total = 0
        for reserva in self.reservas:
            total += reserva.num_diarias * 100  # Exemplo de valor fixo por diária
        return total

# Exemplo de uso da classe Hotel
hotel1 = Hotel("Hotel Estrela")

# Adicionando funcionários ao hotel
hotel1.adicionar_funcionario("João", "Recepcionista", 2500)
hotel1.adicionar_funcionario("Maria", "Camareira", 2000)

# Realizando reservas
hotel1.fazer_reserva("Fulano", 101, 3)  # Exemplo: reserva para o quarto 101 por 3 diárias
hotel1.fazer_reserva("Ciclano", 102, 2)  # Exemplo: reserva para o quarto 102 por 2 diárias

# Calculando a conta final do hotel
conta_final = hotel1.calcular_conta_final()
print(f"Conta final do hotel: R${conta_final:.2f}")
