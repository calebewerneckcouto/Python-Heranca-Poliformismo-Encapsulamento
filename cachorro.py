class Cachorro:
    def __init__(self, nome, raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

class Pessoa:
    def __init__(self,nome,idade,peso,gênero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.gênero = gênero         

class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total_fatura = 0  # Inicialmente o valor total é zero

    def gerar_fatura(self):
        self.valor_total_fatura = self.preco_unitario * self.quantidade

    def imprimir_fatura(self):
        print(f"Nome do Item: {self.nome_item}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Total da Fatura: R${self.valor_total_fatura:.2f}")

# Exemplo de uso da classe Fatura
fatura1 = Fatura("Produto A", 10.5, 3)  # Nome do item, preço unitário, quantidade
fatura1.gerar_fatura()  # Calcula o valor total da fatura

# Imprime a fatura gerada
fatura1.imprimir_fatura()
