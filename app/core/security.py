"""Segurança: funções de hash de senha e verificação de hash.
"""

from _future_ import annotations
from abc import ABC, abstractmethod
import bcrypt
# O bcrypt só considera os primeiros 72 BYTES da senha (e a versão 5 recusa
# senhas maiores). Em UTF-8 um caractere acentuado ocupa 2 bytes, então o limite
# e conferido em bytes, nao em caracteres - ver 'schemas.UsuarioCreate"
LIMITE_BYTES_SENHA = 72
class HashDeSenha (ABC) :
    """Contrato de implementacao de hash de senha. A aplicacao só usa a interface, não
    """
    @abstractmethod
    def gerar(self, senha: str) -> str:
        """Devolve o hash da senha informada."""
    @abstractmethod
    def verificar(self, senha: str, hash_armazenado: str) -> bool:
        """Confere se a senha corresponde ao hash gravado."""
class HashBcrypt (HashDeSenha) :
   """Implementação de hash de senha usando o algoritmo bcrypt.
   """
   def gerar(self, senha: str) -> str:
       return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("ascii")
   def verificar(self, senha: str, hash_armazenado: str) -> bool:
       senha_bytes = senha.encode("utf-8")
       if len(senha_bytes) > LIMITE_BYTES_SENHA:
           # Nenhuma senha cadastrada passa desse tamanho; responder "nao confere"
           # é mais seguro do que deixar o bcrypt lancar um erro inesperado.
           return False
       return bcrypt.checkpw(senha_bytes, hash_armazenado.encode("ascii"))