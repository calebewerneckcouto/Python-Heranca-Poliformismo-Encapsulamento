class Calculadora:
    def somar(self, a, b):
        return a + b

# Exemplos de uso da classe Calculadora
calc = Calculadora()

# Somando dois números inteiros
resultado_int = calc.somar(3, 5)
print(f"Soma de inteiros: {resultado_int}")

# Somando duas strings
resultado_str = calc.somar("Olá ", "Mundo")
print(f"Soma de strings: {resultado_str}")
