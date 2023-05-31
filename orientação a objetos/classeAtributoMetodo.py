class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")


# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 30)
pessoa.falar("Olá!")  # Saída: João diz: Olá!