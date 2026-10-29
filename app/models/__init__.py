"""Modelos de domínio: as entidades do sistema, com seus dados e suas regras.

Cada entidade é responsável por manter o próprio estado valido: o `Usuario`
normaliza o proprio e-mail e so aceita a senha em forma de hash.
"""

# Importar as entidades aqui registra as tabelas no SQLAlchemy (é o que
# `criar_tabelas () usa) e permite escrever from app.models import Usuario`
from app.models.usuario import Usuario

_all_= ["Usuario"]