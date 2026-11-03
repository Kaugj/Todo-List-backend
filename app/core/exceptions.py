"""Exceções de domínio."""
class ErroDeDominio(Exception):
    """Classe base de todo erro previsto de negócio."""
    mensagem = "Nao foi possivel concluir a operacao."
    def _init_(self, mensagem: str | None = None) -> None:
        self.mensagem = mensagem or type(self).mensagem
        super()._init_(self.mensagem)
# ---------------------------------------------------------------------
# Recurso inexistentes - a camada HTTP traduz está familia em 404
# ---------------------------------------------------------------------    
class RecursoNaoEncontrado(ErroDeDominio):
    """Pediram um registro que não existe."""
    
    mensagem = "Recurso não encontrado."
class UsuarioNaoEncontrado(RecursoNaoEncontrado):
    mensagem = "Usuário não encontrado."
# ---------------------------------------------------------------------
# Regra de negócio violada - a camada HTTP traduz está família em 422
# ---------------------------------------------------------------------
class RegraDeNegocioViolada(ErroDeDominio):
    """A operacao é compreensível, mas contraria uma regra do negócio."""
    
    mensagem = "Operacao recusada por uma regra de negocio."
class ValorInvalido(RegraDeNegocioViolada):
    """Valor fora do conjunto aceito por um campo do domínio."""

mensagem = "Valor inválido para o campo."
# ---------------------------------------------------------------------
# Conflito - a camada HTTP traduz em 409
# ---------------------------------------------------------------------
class EmailJaCadastrado(ErroDeDominio):
    """RN_01: um e-mail não pode ser usada por dois usuários.
    A mensagem é a mesma que o front-end já exibe hoje no cadastro.
    """
    mensagem = "Já existe uma conta com este e-mail"
    
class NaoAutenticado(ErroDeDominio):
    """Família dos erros de identidade - a camada HTTP traduz em 401."""
    mensagem = "É preciso entrar na conta para continuar."
    
class CredenciaisInvalidas(NaoAutenticado):
    """E-mail inexistente ou senha incorreta."""
    mensagem = "E-mail ou senha incorretos."
    
class TokenInvalido(NaoAutenticado):
    """Token de acesso ausente, expirado, adulterado ou de usuário removido."""
    mensagem = "Sessão inválida. Entre novamente."