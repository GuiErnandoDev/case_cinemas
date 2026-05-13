from database.connection import ConnectionFactory   


class FilmeRepository:

    def salvar(self, filme):
        connection = ConnectionFactory.get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO filmes (titulo, genero, duracao, classificacao)
            VALUES (?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.genero,
            filme.duracao,
            filme.classificacao
        ))

        connection.commit()
        connection.close()

        print("Filme salvo no banco com sucesso!")

    def listar_filmes(self):

        connection = ConnectionFactory.get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM filmes
        """)

        filmes = cursor.fetchall()

        connection.close()

        return filmes   
    def excluir_filme(self, filme_id):

      connection = ConnectionFactory.get_connection()

      cursor = connection.cursor()
      
      cursor.execute(
        "DELETE FROM filmes WHERE id = ?",
        (filme_id,)
      )

      connection.commit()

      connection.close()