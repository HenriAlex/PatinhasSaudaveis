# Importa o BaseModel do Pydantic.
from pydantic import BaseModel


# Cria o Schema utilizado para receber
# os dados de um perfil.
class PerfilSchema(BaseModel):

    # Descrição do perfil.
    #
    # Exemplos:
    # Dono
    # Dono do Pet
    # Atendente
    # Veterinaria
    # Coordenação
    ds_perfil: str