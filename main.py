
import sys
from rich.console import Console
from InquirerPy import inquirer

import utils   
import autenticacao 
import menus 

console = Console()

def principal():
    try:
        
        utils.inicializar_sistema() 

        while True:
            usuario_logado = autenticacao.login()

            if usuario_logado:
                perfil = usuario_logado.get("perfil")
                
                if perfil == "Coordenador":
                    menus.menu_coordenador(usuario_logado)
                elif perfil == "Professor":
                    menus.menu_professor(usuario_logado)
                elif perfil == "Aluno":
                    menus.menu_aluno(usuario_logado)
                else:
                    console.print("[bold red]Erro: Perfil de usuário desconhecido.[/bold red]")
                    utils.pausar_tela()
            
            else:
                tentar_de_novo = inquirer.confirm(
                    message="Deseja tentar o login novamente?",
                    default=True
                ).execute()
                
                if not tentar_de_novo:
                    console.print("[cyan]Até logo![/cyan]")
                    break
                    
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Saindo...")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Ocorreu um erro inesperado: {e}[/bold red]")
        console.print("O programa será encerrado.")
        sys.exit(1)

if __name__ == "__main__":
    principal()
