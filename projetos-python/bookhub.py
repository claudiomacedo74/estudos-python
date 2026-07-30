import os

livros= [{'titulo':'Dom Casmurro', 'autor':'Machado de Assis', 'emprestado': False},
 {'titulo':'O Pequeno Príncipe', 'autor':'Antoine de Saint-Exupéry', 'emprestado': True},
 {'titulo':'1984', 'autor':'George Orwell', 'emprestado': False},
 {'titulo':'O Senhor dos Anéis', 'autor':'J.R.R. Tolkien', 'emprestado': False},
 {'titulo':'Harry Potter', 'autor':'J.K. Rowling', 'emprestado': True}]


def exibir_titulo():
    print('BookHub\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_opcoes():  
    print('1.Cadastrar livro ')
    print('2.Listar Livros')
    print('3.Emprestar/devolver livro')
    print('4.Buscar livro')
    print('5.Remover livro')
    print('6.Sair')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
          cadastrar_livros()
        elif opcao_escolhida == 2:
          listar_livros()
        elif opcao_escolhida == 3:
           emprestar_devolver_livros()
        elif opcao_escolhida == 4:
           buscar_livros()
        elif opcao_escolhida == 5:
            remover_livro()
        elif opcao_escolhida == 6:
            finalizar_app()
    except:
       opcao_invalida()
           

def livro_nao_encontrado():
    print('O livro digitado não existe')
    voltar_menu_principal()
          

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_menu_principal():
   print('Digite uma tecla para voltar para o menu principal')
   input()
   main()

def cadastrar_livros():
    exibir_subtitulo('Cadastro de novos livros')
    nome_livro = input('Digite o titulo do livro que deseja cadastrar: ')
    autor_livro = input('Digite o autor do livro: ')
    livros.append
    print(f'O Livro {nome_livro} foi cadastrado com sucesso!')
    voltar_menu_principal()
    main()

def listar_livros():
    exibir_subtitulo('Lista de livros cadastrados')
    print(f'{'Livro'.ljust(22)} {'Autor'.ljust(20)} {'Status'}\n')
    for livro in livros:
        nome_livro = livro['titulo']
        autor_livro = livro['autor']
        emprestado = livro['emprestado']
        print(f'{nome_livro.ljust(20)} | {autor_livro.ljust(20)} | {"Emprestado" if emprestado else "Disponível"}')

def emprestar_devolver_livros():
   exibir_subtitulo('Empréstimo/Devolução de itens')
   titulo = input('Digite o titulo do livro que deseja pegar/devolver: ')
   livro_encontrado = False
   for livro in livros:
    if titulo == livro['titulo']:
     livro_encontrado = True 
     if livro['emprestado']:
      print(f'O livro {titulo} foi devolvido com sucesso')
     else:
      print(f'O livro {titulo} foi emprestado com sucesso')
     livro['emprestado'] = not livro['emprestado']
     break
    if not livro_encontrado:
      livro_nao_encontrado()

def buscar_livros():
   exibir_subtitulo('Busca De Livros')
   livro_encontrado = False
   busca = input('Digite o nome do livro que deseja buscar: ')
   for livro in livros:
     if busca == livro['titulo']:   
       livro_encontrado = True
       print(f"Titulo: {livro['titulo']}")
       print(f"Autor: {livro['autor']}")
       print(f"Status: {'Emprestado' if livro ['emprestado'] else 'Disponivel'}")
       break
   if not livro_encontrado:
     livro_nao_encontrado() 

def remover_livro():
   exibir_subtitulo('Remoção de livros')
   livro_encontrado = False
   busca = input('Digite o nome do livro que deseja remover: ')
   for livro in livros:
      if busca == livro['titulo']:
        livro_encontrado = True
        livros.remove(livro)
        print(f'O livro "{busca}" foi removido com sucesso!')
        break
   if not livro_encontrado:
        livro_nao_encontrado()      

def opcao_invalida():
   print('Opção Invalida! ')
   voltar_menu_principal()
          


def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
  
  
