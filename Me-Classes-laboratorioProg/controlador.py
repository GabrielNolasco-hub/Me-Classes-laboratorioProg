from entidades import Cadastro

registros = []


def cadastrar_usuario(nome: str, idade: int, cidade: str) -> Cadastro:
    pessoa = Cadastro(nome, idade, cidade)
    registros.append(pessoa)
    return pessoa


def listar_usuarios() -> list[str]:

    return [str(p) for p in registros]


def editar_usuario(indice: int, nome: str = None, idade: int = None, cidade: str = None) -> Cadastro | None:

    if 0 <= indice < len(registros):
        pessoa = registros[indice]
        if nome is not None:
            pessoa.mudar_nome(nome)
        if idade is not None:
            pessoa.mudar_idade(idade)
        if cidade is not None:
            pessoa.mudar_cidade(cidade)
        return pessoa
    return None

def deletar_usuario(indice: int) -> Cadastro | None:

    if 0 <= indice < len(registros):
        return registros.pop(indice)
    return None