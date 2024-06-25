class Carro:
    def __init__(self, modelo, cor, ano, velocidade_maxima):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self, velocidade):
        self.velocidade += velocidade
        print(f"O carro está agora a {self.velocidade} km/h")

    def frear(self, velocidade):
        if self.velocidade >= velocidade:
            self.velocidade -= velocidade
            print(f"O carro está agora a {self.velocidade} km/h após frear")
        else:
            print('O carro já está parado')

# Criando uma instância da classe Carro
orochino = Carro("Sentra", "Prata", 2020, 120)

# Testando a saída
print(orochino.modelo)  # Saída: Sentra

orochino.acelerar(120)
orochino.frear(30)
