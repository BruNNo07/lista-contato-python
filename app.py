import functions

while True:
    print('''
        1. Adicionar Contato
        2. Visualizar lista de contatos
        3. Editar Contato.
        4. Marcar/Desmarcar contato como favorito.
        5. Visualizar lista de contatos favoritos.
        6. Apagar contato.
    ''')
    escolha = int(input("""Digite o numero da ação que deseja fazer: """))
    print("")
    print("")

    if escolha == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')
        functions.AdicionarContato(nome,telefone,email)
    elif escolha == 2:
        functions.VisualizarContatos()
    elif escolha == 3:
        functions.VisualizarContatos()
        indiceContato = input('Digite o indice respectivo ao contato: ')
        functions.EditarContato(indiceContato)
    elif escolha == 4:
        functions.VisualizarContatos()
        indiceContato = input('Digite o indice respectivo ao contato: ')
        functions.MarcarDesmarcarFavorito(indiceContato)
    elif escolha == 5:
        functions.VisualizarFavoritos()
    elif escolha == 6:
        indiceContato = input('Digite o indice respectivo ao contato: ')
        functions.DeletarContato(indiceContato)

