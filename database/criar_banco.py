# Importa a classe responsável pela conexão com o banco.
from database.conexao import Conexao


# Classe responsável pela criação do banco
# e das tabelas do sistema.
class CriarBanco:

    # Método estático.
    # Pode ser executado sem criar um objeto da classe.
    @staticmethod
    def criar():

        # Abre uma conexão com o banco SQLite.
        #
        # Caso o arquivo saidinha.db não exista,
        # o SQLite irá criá-lo automaticamente.
        conexao = Conexao.conectar()

        # Cria um cursor para executar comandos SQL.
        cursor = conexao.cursor()

        # Cria a tabela PERFIL caso ela ainda não exista.
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS perfil (
            id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
            ds_perfil VARCHAR(200) NOT NULL
        );

        """)

        # Cria a tabela USUARIO caso ela ainda não exista.
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            ra VARCHAR(20) NOT NULL,
            nome VARCHAR(150) NOT NULL,
            id_perfil INTEGER NOT NULL,
            email VARCHAR(150) NOT NULL,
            senha VARCHAR(100) NOT NULL,
            data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

            CONSTRAINT fk_usuario_perfil
                FOREIGN KEY (id_perfil)
                REFERENCES perfil(id_perfil)
        );

        """)

        # Confirma as alterações realizadas no banco.
        conexao.commit()

        # Fecha a conexão com o banco.
        conexao.close()


# Executa o método responsável por criar
# o banco de dados e suas tabelas.
CriarBanco.criar()