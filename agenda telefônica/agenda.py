class Contato:
  nome: str
  telefone: int
  idade: int

def menu():
  
  menu = '''
=============
    MENU
=============
Digite o número da opção que deseja realizar com os contatos:
(1) Cadastrar novo contato
(2) Localizar contato
(3) Alterar contato
(4) Excluir contato
(5) Listar seus contatos
'''
  
  print(menu)
  N = int(input())
  return N


def opcoes(N, lista):
  if N == 1:
    return contatos(lista)
  if N == 2:
    localizar(lista)
    return lista
  if N == 3:
    return alterar(lista)
  if N == 4:
    return excluir(lista)
  if N == 5:
    mostrar(lista)
    return lista


def contatos(lista: list) -> list:
    ctt = Contato()
    ctt.nome = input('NOME\n')
    ctt.telefone = int(input('TELEFONE\n'))
    ctt.idade = int(input('IDADE\n'))
    lista.append(ctt)
    return lista


def localizar(lista: list) -> None:
  L = input('Digite o nome do contato\n')
  for i in range(len(lista)):
    if L == lista[i].nome:
      print(f'\nTelefone: {lista[i].telefone}\nIdade: {lista[i].idade}')


def alterar(lista: list) -> list:
  L = input('\nDigite o nome do contato\n')
  D = int(input('\nQual informação deseja alterar?\n(1) Nome\n(2) Telefone\n(3) Idade\n'))
  for i in range(len(lista)):
    if L == lista[i].nome:
      if D == 1:
        lista[i].nome = input('\nDigite o novo nome\n')
      elif D == 2:
        lista[i].telefone = int(input('\nDigite o novo telefone\n'))
      elif D == 3:
        lista[i].idade = int(input('\nDigite a nova idade\n'))
      break
  return lista


def excluir(lista: list) -> list:
  N = input('\nInforme o nome do contato que deseja excluir\n')
  for i in range(len(lista)):
    if lista[i].nome == N:
      del lista[i]
      break
  return lista


def mostrar(lista: list) -> None:
  for i in range(len(lista)):
    print('NOME:', lista[i].nome)
    print('TELEFONE:', lista[i].telefone)
    print('IDADE:', lista[i].idade)
    print()


lista_contatos = []
while True:
  N = menu()
  lista = opcoes(N, lista_contatos)
