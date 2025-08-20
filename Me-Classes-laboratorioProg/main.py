from controlador import cadastrar_usuario, listar_usuarios, editar_usuario, deletar_usuario


cadastrar_usuario("Ana", 22, "Sao Paulo")
cadastrar_usuario("pedro", 37, "Maceió")
cadastrar_usuario("joao", 25, "Rio de Janeiro")

print("Lista de usuarios:")
print(listar_usuarios())



editar_usuario(1, cidade="rio de janeiro")

deletar_usuario(2)

print("Lista de usuarios pós alteração:")
print(listar_usuarios())





