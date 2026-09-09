from datetime import datetime

class Usuario:

    def __init__(
        self, 
        id_usuario = 0,
        nome = "",
        id_perfil = 0,
        cadastro = None,
        email = "",
        senha = ""):

        # Código identificador do usuário.
        self.id_usuario = id_usuario

        # Código do perfil do usuário.
        self.id_perfil = id_perfil
        
        # Nome completo do usuário.
        self.nome = nome
        
        # E-mail utilizado para login.
        self.email = email
        
        # Senha do usuário.
        self.senha = senha
        
        # Caso nenhuma data seja informada,
        # utiliza a data e hora atuais.
        if cadastro is None:
            self.cadastro = datetime.now()
        else:
            self.cadastro = cadastro