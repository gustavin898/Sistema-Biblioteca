
from catalogo import (
    adicionar_livro,
    listar_catalogo,
    buscar_livro,
    remover_livro,
    atualizar_estoque
)

from relatorios import gerar_relatorio


def menu():
    while True:
        print("\n================================")
        print("   SISTEMA DE GERENCIAMENTO")
        print("          BIBLIOTECA")
        print("================================")
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Remover livro")
        print("5 - Atualizar estoque")
        print("6 - Gerar relatório e gráfico")
        print("0 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            autor = input("Autor: ").strip()
            genero = input("Gênero: ").strip()

            try:
                quantidade = int(
                    input("Quantidade em estoque: ")
                )

                if not titulo or not autor or not genero:
                    print("Preencha todos os campos.")
                else:
                    adicionar_livro(
                        titulo, autor, genero, quantidade
                    )

            except ValueError:
                print("Digite uma quantidade válida.")

        elif opcao == "2":
            listar_catalogo()

        elif opcao == "3":
            titulo = input("Digite o título para buscar: ")
            buscar_livro(titulo)

        elif opcao == "4":
            titulo = input("Digite o título para remover: ")
            remover_livro(titulo)

        elif opcao == "5":
            titulo = input("Digite o título do livro: ")

            try:
                quantidade = int(
                    input("Nova quantidade em estoque: ")
                )

                atualizar_estoque(titulo, quantidade)

            except ValueError:
                print("Digite uma quantidade válida.")

        elif opcao == "6":
            gerar_relatorio()

        elif opcao == "0":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
