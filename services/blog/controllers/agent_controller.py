from typing import List
from services.blog.repository.agent_repo import AgentRepo
from services.blog.models.agent_model import AgentUpdate, AgentCreate, AgentRead
from fastapi import HTTPException, status
from .blog_constant import blog_const


def update_agent(id: int, agent: AgentUpdate) -> AgentRead:
    updated_agent = AgentRepo().update_agent(id, agent)
    if not updated_agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.AGENT_NOT_FOUND)
    return updated_agent


def add_agent(agent: AgentCreate) -> AgentRead:
    return AgentRepo().add_agent(agent)


def get_agent(id: int) -> AgentRead:
    agent = AgentRepo().get_agent(id)
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.AGENT_NOT_FOUND)
    return agent


def get_all_agents(offset: int, limit: int) -> List[AgentRead]:
    agents = AgentRepo().get_all_agents(offset, limit)
    if not agents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.NO_AGENT_EXIST)
    return agents


def detete_agent(id: int):
    detete_result = AgentRepo().delete_agent(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.AGENT_NOT_FOUND)
    return detete_result
