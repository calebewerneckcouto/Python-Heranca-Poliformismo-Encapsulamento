from abc import ABC, abstractmethod

# Definição da interface Veiculo
class Veiculo(ABC):
    
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass

# Classe concreta Carro que implementa Veiculo
class Carro(Veiculo):
    
    def acelerar(self):
        print("Carro acelerando...")
    
    def frear(self):
        print("Carro freando...")

# Classe concreta Bicicleta que implementa Veiculo
class Bicicleta(Veiculo):
    
    def acelerar(self):
        print("Bicicleta pedalando...")
    
    def frear(self):
        print("Bicicleta freando...")

# Função para simular a interação com veículos
def testar_veiculo(veiculo):
    veiculo.acelerar()
    veiculo.frear()

# Exemplos de uso do polimorfismo
carro = Carro()
bicicleta = Bicicleta()

print("Testando carro:")
testar_veiculo(carro)

print("\nTestando bicicleta:")
testar_veiculo(bicicleta)
