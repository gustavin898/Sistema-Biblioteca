
from livros import Livro

catalogo = []


def adicionar_livro(titulo, autor, genero, qtd_estoque):
    if qtd_estoque < 0:
        print("A quantidade não pode ser negativa.")
        return

    for livro in catalogo:
        if livro.titulo.lower() == titulo.lower():
            print("Este livro já está cadastrado.")
            return

    novo_livro = Livro(titulo, autor, genero, qtd_estoque)
    catalogo.append(novo_livro)

    print(f"Livro '{titulo}' adicionado com sucesso!")


def listar_catalogo():
    print("\n===== CATÁLOGO DA BIBLIOTECA =====")

    if not catalogo:
        print("Nenhum livro cadastrado.")
        return

    for livro in catalogo:
        print(livro)


def buscar_livro(titulo):
    for livro in catalogo:
        if livro.titulo.lower() == titulo.lower():
            print("\nLivro encontrado:")
            print(livro)
            return livro

    print("Livro não encontrado.")
    return None


def remover_livro(titulo):
    for livro in catalogo:
        if livro.titulo.lower() == titulo.lower():
            catalogo.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso!")
            return

    print("Livro não encontrado.")


def atualizar_estoque(titulo, quantidade):
    if quantidade < 0:
        print("A quantidade não pode ser negativa.")
        return

    livro = buscar_livro(titulo)

    if livro is not None:
        livro.qtd_estoque = quantidade
        print("Estoque atualizado com sucesso!")
