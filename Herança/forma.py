import math

class Forma:
    def calcular_area(self):
        pass  # Este método será implementado nas classes derivadas
    
    def calcular_perimetro(self):
        pass  # Este método será implementado nas classes derivadas

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

# Exemplos de uso das classes
circulo = Circulo(5)
print("Área do círculo:", circulo.calcular_area())
print("Perímetro do círculo:", circulo.calcular_perimetro())

retangulo = Retangulo(4, 6)
print("Área do retângulo:", retangulo.calcular_area())
print("Perímetro do retângulo:", retangulo.calcular_perimetro())
