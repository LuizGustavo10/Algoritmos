class Carro:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo privado

    def mostrar_marca(self):
        print(self._marca)

    def mostrar_modelo(self):
        print(self._modelo)

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla")
meu_carro.mostrar_marca()  # Saída: Toyota
meu_carro.mostrar_modelo()  # Saída: Corolla
print(meu_carro._marca)  # Saída: Toyota
print(meu_carro._modelo)  # Erro: AttributeError: 'Carro' object has no attribute '__modelo'