
class Livro:
    def __init__(self, titulo, autor, genero, qtd_estoque):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtd_estoque = qtd_estoque

    def __str__(self):
        return (
            f"{self.titulo} por {self.autor} | "
            f"Gênero: {self.genero} | "
            f"Estoque: {self.qtd_estoque}"
        )
