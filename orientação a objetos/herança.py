class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veículo está ligado.")

    def desligar(self):
        print("O veículo está desligado.")

    def falar(self):
        print(f"{self.marca} diz: {self.modelo}")



class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def abrir_porta(self):
        print("Uma porta do carro foi aberta.")

# Criando uma instância da classe Carro

veiculo = Veiculo("vw", "GOL")

veiculo.falar()  # Saída: João diz: Olá!

meu_carro = Carro("Toyota", "Corolla", 4)
print(meu_carro.marca)        # Saída: Toyota
print(meu_carro.num_portas)   # Saída: 4
meu_carro.ligar()             # Saída: O veículo está ligado.