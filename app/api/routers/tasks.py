"""Endpoint de tarefas: todos exigem login.

o dono das tarefas é sempre quem está auteenticado (vem do venv). Não existe mais `usuarioId` na URL nem no corpo: antes, bastava trocar esse número para
ler, alterar ou apagar a tarefa de outra pessoa.
"""


from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import UsuarioAtual, obter_tarefa_servico
from app.schemas import TarefaCreate, TarefaOut
from app.services import TarefaServico

router = APIRouter(
    prefix="/tasks",
    tags=["tarefas"],
    responses={401: {"description": "Sem token, ou token inválido/expirado"}},
)

Servico = Annotated[TarefaServico, Depends(obter_tarefa_servico)]


@router.post(
    "",
    response_model=TarefaOut,
    status_code=status.HTTP_201_CREATED,
    summary="Criar tarefa",
)
def criar_tasks(dados: TarefaCreate, usuario: UsuarioAtual, servico: Servico) -> TarefaOut:
    """Cria uma tarefa para o usuário logado. Nasce sempre pendente."""
    return servico.criar(
        usuario_id=usuario.id,
        titulo=dados.titulo,
        prioridade=dados.prioridade,
        prazo=dados.prazo,
    )