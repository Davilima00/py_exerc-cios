import pydoc
from termcolor import colored

def mostrar_manual(comando):
    try:
        help_info = pydoc.plain(pydoc.render_doc(comando))
        print(colored(help_info, 'green'))
    except Exception as e:
        print(colored(f'Erro ao acessar o manual: {e}', 'red'))

def main():
    while True:
        comando = input(colored('Digite o comando (ou "FIM" para sair): ', 'blue'))
        
        if comando.upper() == 'FIM':
            print(colored('Sistema encerrado.', 'yellow'))
            break

        mostrar_manual(comando)

if __name__ == "__main__":
    main()
