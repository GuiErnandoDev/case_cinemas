from src.repositories.filme_repository import FilmeRepository


class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrar_filme(self, filme):

        if filme.titulo == "":
            print("Título inválido!")
            return

        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar_filmes()
    def excluir_filme(self, filme_id):
        self.repository.excluir_filme(filme_id)