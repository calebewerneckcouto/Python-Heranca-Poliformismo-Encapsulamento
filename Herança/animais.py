# Classe base Animal
class Animal:
    def emitirSom(self):
        pass  # Método a ser sobrescrito nas classes derivadas

# Classes derivadas: Cachorro, Gato e Pássaro
class Cachorro(Animal):
    def emitirSom(self):
        return "Au au!"

class Gato(Animal):
    def emitirSom(self):
        return "Miau!"

class Passaro(Animal):
    def emitirSom(self):
        return "Piu piu!"

# Criando uma lista de animais
animais = [Cachorro(), Gato(), Passaro()]

# Percorrendo a lista e chamando o método emitirSom de cada animal
for animal in animais:
    print(animal.emitirSom())
