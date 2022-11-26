from typing import List
from fastapi import APIRouter, status, Query

from services.blog.models.agent_model import AgentRead, AgentCreate, AgentUpdate
import services.blog.controllers.agent_controller as agent_controller


router = APIRouter(
    prefix="/agents",
    tags=['agent']
)


@router.post("/",
             response_model=AgentRead,
             status_code=status.HTTP_201_CREATED
             )
def add_agent(*, agent: AgentCreate):
    return agent_controller.add_agent(agent)


@router.get("/",
            response_model=List[AgentRead],
            status_code=status.HTTP_200_OK
            )
def get_all_agents(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return agent_controller.get_all_agents(offset, limit)


@router.get("/{id}",
            response_model=AgentRead,
            status_code=status.HTTP_200_OK
            )
def get_agent(*, id: int):
    return agent_controller.get_agent(id)


@router.patch("/{team_id}",
              response_model=AgentRead,
              status_code=status.HTTP_200_OK
              )
def update_agent(
    *,
    id: int,
    agent: AgentUpdate,
):
    return agent_controller.update_agent(id, agent)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def detete_agent(*, id: int):
    return agent_controller.detete_agent(id)
