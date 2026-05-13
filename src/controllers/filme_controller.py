from src.models.filme import Filme
from src.services.filme_service import FilmeService


class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar_filme(self):

        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = int(input("Duração (em minutos): "))
        classificacao = input("Classificação: ")

        filme = Filme(
            titulo,
            genero,
            duracao,
            classificacao
        )

        self.service.cadastrar_filme(filme)

    def listar_filmes(self):

        filmes = self.service.listar_filmes()

        print("\nLISTA DE FILMES\n")

        for filme in filmes:
            print(f"""
ID: {filme[0]}
Título: {filme[1]}
Gênero: {filme[2]}
Duração: {filme[3]} min
Classificação: {filme[4]}
            """)

    def excluir_filme(self):

        filme_id = int(input("ID do filme que deseja excluir: "))

        self.service.excluir_filme(filme_id)

        print("\nFilme excluído com sucesso!\n")