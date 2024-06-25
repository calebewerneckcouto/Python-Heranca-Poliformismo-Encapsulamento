class Animal:
    def __init__(self,nome):
        self.nome = nome
    def fazerSom(self):
        pass

class Cachorro(Animal):
    def fazerSom(self):
        return "Au Au"


class Gato(Animal):
    def fazerSom(self):
        return "Miauuuu"
    
Luke = Cachorro("Luke")   
gatuno = Gato("gatuno")

print(Luke.nome,"faz",Luke.fazerSom())
print(gatuno.nome,"faz",gatuno.fazerSom())