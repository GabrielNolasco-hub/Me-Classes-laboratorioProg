class Cadastro:
    def __init__(self, nome:str, idade:int, cidade:str):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


    def mudar_nome(self, novo_nome:str):
        self.nome = novo_nome


    def mudar_idade(self, nova_idade:int):
        self.idade = nova_idade


    def mudar_cidade(self, nova_cidade:str):
        self.cidade = nova_cidade        



    def __str__(self):
        return f"{self.nome} ({self.idade}) - {self.cidade}"    