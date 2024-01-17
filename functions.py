lista = []

def AdicionarContato(nome, telefone, email):
    contato = {"nome": nome, 'telefone': telefone, 'email': email, 'favorito': False}
    lista.append(contato)
    print("Contato adicionado.")
    return

def VisualizarContatos():
    print('Lista de contatos:')

    if(len(lista) == 0):
        print("\n Lista de contatos vazia.")

    for indice, contato in enumerate(lista):
        indice = indice + 1
        favorito = '*' if contato['favorito'] else ' '
        print(f"{indice}. [{favorito}] {contato['nome']} | {contato['telefone']} | {contato['email']}")
    return

def EditarContato(indice):
    indice = int(indice) - 1
    
    if indice < 0:
        return
    
    print(f"{lista[indice]['nome']} | {lista[indice]['telefone']} | { lista[indice]['email'] }")
    print('''
        O que Deseja alterar?

        1. Nome
        2. Telefone
        3. Email
          
    ''')
    escolha = int(input('Digite uma opção: '))

    if escolha == 1:
        novoNome = input('Digite o novo nome: ')
        lista[indice]['nome'] = novoNome
    elif escolha == 2:
        novoTelefone = input('Digite o novo telefone: ')
        lista[indice]['telefone'] = novoTelefone
    elif escolha == 3:
        novoEmail = input('Digite o novo email: ')
        lista[indice]['email'] = novoEmail
    else:
        print('A opção que você escolheu não esta disponivel.')

def MarcarDesmarcarFavorito(indice):
    indice = int(indice) - 1
    if lista[indice]['favorito']:
        lista[indice]['favorito'] = False
    else:
        lista[indice]['favorito'] = True

def VisualizarFavoritos():
    for contato in lista:
        if contato['favorito']:
            print(f"[*] {contato['nome']} | {contato['telefone']} | { contato['email'] }")

def DeletarContato(indice):
    indice = int(indice) - 1
    for index, contato in enumerate(lista):
        if index == indice:
            lista.remove(contato)