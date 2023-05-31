class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz au au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz miau!")

# Função que recebe um objeto Animal e chama o método fazer_som
def fazer_barulho(animal):
    animal.fazer_som()

# Criando instâncias das classes Cachorro e Gato
meu_cachorro = Cachorro()
meu_gato = Gato()

fazer_barulho(meu_cachorro)   # Saída: O cachorro faz au au!
fazer_barulho(meu_gato)       # Saída: O gato faz miau!