nome_arquivo = 'agenda.txt'
arquivo = open(nome_arquivo, 'a')
arquivo.close()


class Contato:
  nome: str
  telefone: int
  adicional: str

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
  elif N == 2:
    localizar(lista)
    return lista
  elif N == 3:
    return alterar(lista)
  elif N == 4:
    return excluir(lista)
  elif N == 5:
    mostrar(lista)
    return lista


def contatos(lista: list) -> list:
    ctt = Contato()
    ctt.nome = input('NOME\n')
    ctt.telefone = int(input('TELEFONE\n'))
    ctt.adicional = input('INFORMAÇÃO ADICIONAL\n')
    lista.append(ctt)
    gravar_arquivo(nome_arquivo, lista)
    return lista


def localizar(lista: list) -> None:
  L = input('Digite o nome do contato\n')
  for i in range(len(lista)):
    if L == lista[i].nome:
      print(f'\nTelefone: {lista[i].telefone}\nIdade: {lista[i].idade}')


def alterar(lista: list) -> list:
  L = input('\nDigite o nome do contato\n')
  D = int(input('\nQual informação deseja alterar?\n(1) Nome\n(2) Telefone\n(3) Inf. adicional\n'))
  for i in range(len(lista)):
    if L == lista[i].nome:
      if D == 1:
        lista[i].nome = input('\nDigite o novo nome\n')
      elif D == 2:
        lista[i].telefone = int(input('\nDigite o novo telefone\n'))
      elif D == 3:
        lista[i].adicional = input('\nDigite a nova informação\n')
      break
  gravar_arquivo(nome_arquivo, lista)
  return lista


def excluir(lista: list) -> list:
  N = input('\nInforme o nome do contato que deseja excluir\n')
  for i in range(len(lista)):
    if lista[i].nome == N:
      del lista[i]
      break
  gravar_arquivo(nome_arquivo, lista)
  return lista


def mostrar(lista: list) -> None:
  for i in range(len(lista)):
    print('NOME:', lista[i].nome)
    print('TELEFONE:', lista[i].telefone)
    print('INF. ADICIONAL:', lista[i].adicional)
    print()

def ler_arquivo(nome_arquivo: str) -> list:
  arquivo = open(nome_arquivo, 'r')
  lista = []
  for linha in arquivo.readlines():
    C = Contato()
    linha = linha.replace('\n', '')
    posicao = linha.split('##')
    C.nome = posicao[0]
    C.telefone = posicao[1]
    C.adicional = posicao[2]
    lista.append(C)
  arquivo.close()
  return lista


def gravar_arquivo(nome_arquivo: str, lista: list):
  arquivo = open(nome_arquivo, 'w')
  for i in range(len(lista_contatos)):
    L = f'{lista[i].nome}##{lista[i].telefone}##{lista[i].adicional}\n'
    arquivo.write(L)
  arquivo.close()
  

lista_contatos = ler_arquivo(nome_arquivo)
while True:
  N = menu()
  lista = opcoes(N, lista_contatos)
