class Retangulo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento
        self._largura = largura

    @property
    def area(self):
        return self._comprimento * self._largura

    @property
    def comprimento(self):
        return self._comprimento

    @comprimento.setter
    def comprimento(self, novo_comprimento):
        if novo_comprimento > 0:
            self._comprimento = novo_comprimento

# Criando uma instância da classe Retangulo
retangulo = Retangulo(5, 3)
print(retangulo.area)         # Saída: 15
print(retangulo.comprimento)  # Saída: 5

retangulo.comprimento = 10    # Usando o setter
print(retangulo.comprimento)  # Saída: 10