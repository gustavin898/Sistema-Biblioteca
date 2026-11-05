
import matplotlib.pyplot as plt
from catalogo import catalogo


def gerar_relatorio():
    if not catalogo:
        print("Não existem livros para gerar o relatório.")
        return

    total_livros = sum(
        livro.qtd_estoque for livro in catalogo
    )

    print("\n===== RELATÓRIO DA BIBLIOTECA =====")
    print(f"Total de livros em estoque: {total_livros}")

    generos = {}

    for livro in catalogo:
        genero = livro.genero.strip().title()

        if genero in generos:
            generos[genero] += livro.qtd_estoque
        else:
            generos[genero] = livro.qtd_estoque

    print("\nQuantidade por gênero:")

    for genero, quantidade in generos.items():
        print(f"{genero}: {quantidade} unidades")

    plt.figure(figsize=(9, 5))

    plt.bar(
        generos.keys(),
        generos.values()
    )

    plt.title("Quantidade de Livros por Gênero")
    plt.xlabel("Gêneros")
    plt.ylabel("Quantidade em Estoque")

    plt.tight_layout()
    plt.show()
