"""Exceções de domínio (ou de negócio) da applicação.
"""
class ErroDominio(Exception):
    """Classe base de todo erro previsto de negócio.
    
    A mensagem padrão fica na classe para que quem lança a exceção não precise
    repeti-la em cada `raise`, mas possa sobrecrevê-la quando houver um
    detalhe útil a acrescentatar.
    """
    mensagem = "Nao foi possivel concluir a operacao."

    def _init_(self, mensagem: str | None = None) -> None:
        self.mensagem = mensagem or type(self).mensagem
        super()._init_(self.mensagem)
class RegraDeNegocioViolada(ErroDeDominio):
    """A operacao é compreensível, mas contraria uma regra do negócio."""
    mensagem = "Operacao recusada por uma regra de negocio."
class ValorInvalido(RegraDeNegocioViolada):
    """Valor fora do conjunto aceito por um campo do domínio."""

mensagem = "Valor inválido para o campo."