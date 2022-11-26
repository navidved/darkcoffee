from sqlmodel import select

from core.database import Database
from services.blog.models.agent_model import AgentModel, AgentRead, AgentPassUpdate, AgentCreate, AgentUpdate


class AgentRepo:
    def add_agent(self, agent: AgentCreate) -> AgentRead:
        from core.hashing import get_password_hash
        db_agent = AgentModel.from_orm(agent)
        db_agent.hashed_password = get_password_hash(agent.password)
        session = Database().get_session()
        session.add(db_agent)
        session.commit()
        session.refresh(db_agent)
        return db_agent

    def get_agent(self, id: int) -> AgentRead:
        session = Database().get_session()
        return session.get(AgentModel, id)

    def get_all_agents(self, offset: int, limit: int) -> list[AgentRead]:
        session = Database().get_session()
        statement = select(AgentModel).offset(offset).limit(limit)
        agents = session.exec(statement).all()
        return agents

    def update_agent(self, id: int, agent: AgentUpdate) -> AgentRead:
        session = Database().get_session()
        db_agent = session.get(AgentModel, id)
        if not db_agent:
            return None

        agent_data = agent.dict(exclude_unset=True)
        for key, value in agent_data.items():
            setattr(db_agent, key, value)

        session.add(db_agent)
        session.commit()
        session.refresh(db_agent)
        return db_agent

    def delete_agent(self, id: int) -> bool:
        session = Database().get_session()
        agent = session.get(AgentModel, id)
        if not agent:
            return False
        session.delete(agent)
        session.commit()
        return True

def get_agent_by_username(username: str):
    statement = select(AgentModel).where(AgentModel.username == username)
    session = Database().get_session()
    agent = session.exec(statement).first()
    return agent
