import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Hut', 'categoria':'Pizza', 'ativo':True},
                {'nome':'MCDonald', 'categoria':'Hamburger', 'ativo':False}]

def exibir_titulo():
    '''Exibe o nome/titulo do programa na tela'''
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    '''Essa funçao e responsavel pela exibiçao dos subtitulo nas opçoes escolhidas e por limpar as tela '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    '''Responsavel por exibir as opçoes disponiveis pro user'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Mudar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Responsavel por finalizar o app'''
    exibir_subtitulo('Finalizando app')

def voltar_menu_pricipal():
     '''responsavel a fazer o usuarioi digitar alguma tecla para voltar ao menu principal'''
     print(' \nDigite uma tecla para voltar ao menu: ')
     input()
     main()

def opcao_invalida():
   '''Responsavel por caso o usuario digite uma opçao invalida ele volte para o menu principal'''
   print('Opcao invalida!!!\n')
   voltar_menu_pricipal()


def cadastrar_novo_restaurante():
  '''inputs:
  -Nome do restaurante
  -Categoria restaurante
  
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_restaurante = input('Digite o nome do Restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}:')
  dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
  restaurantes.append(dados_do_restaurante)  
  print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
  voltar_menu_pricipal()
  main()

def listar_restaurantes():
    '''Responsavel por mostrar as informaçoes dos restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes cadastrados')
    
    print(f'{'Nome do restaurante'.ljust(22)}   {'Categoria'.ljust(20)}   {'Estado'}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'-{nome_restaurante.ljust(20)}| {categoria.ljust(20)} | {"Ativo" if ativo else "Inativo"}')
    voltar_menu_pricipal()
    main()
    
def alternar_estado_r():
    '''Inputs
    -Alternar Estado Do Restaurante
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja mudar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if  nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'o restaurante {nome_restaurante} foi ativado ' 
        if restaurante ['ativo'] else f'O restaurante foi desativado')
        print(mensagem) 
        if not restaurante_encontrado:
         print('O restaurante nao foi encontrado')   

def escolher_opcao():
    '''responsavel por pela erxecuçao da aopçau escolhida pelo user''' 
    try:     
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
           listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_r()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
       opcao_invalida()

def main():
   '''Funçao principal que inicia o programa e exibe o titulo,subtitulo e as opçoes'''
   os.system('cls')
   exibir_titulo()
   exibir_opcoes() 
   escolher_opcao()
  

if __name__ == '__main__':
    main()


    