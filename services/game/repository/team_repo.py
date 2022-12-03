from sqlmodel import select
from core.database import Database

from services.game.models.team_model import TeamModel, TeamCreate, TeamRead, TeamUpdate
from services.blog.models.agent_model import AgentRead


class TeamRepo:

    def add_team(self,
                 team: TeamCreate,
                 current_user: AgentRead
                 ) -> TeamModel:
        session = Database().get_session()
        db_team = TeamModel.from_orm(team)
        db_team.agent_id = current_user.id
        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team

    def get_all_teams(self,
                      offset: int,
                      limit: int
                      ) -> list[TeamRead]:
        session = Database().get_session()
        statement = select(TeamModel).offset(offset).limit(limit)
        teams = session.exec(statement).all()
        return teams

    def get_team(self,
                 id: int
                 ) -> TeamRead:
        session = Database().get_session()
        return session.get(TeamModel, id)

    def update_team(self,
                    id: int,
                    team: TeamUpdate
                    ) -> TeamRead:
        session = Database().get_session()
        db_team = session.get(TeamModel, id)
        if not db_team:
            return None

        team_data = team.dict(exclude_unset=True)
        for key, value in team_data.items():
            setattr(db_team, key, value)

        session.add(db_team)
        session.commit()
        session.refresh(db_team)
        return db_team

    def delete_team(self,
                    id: int) -> bool:
        session = Database().get_session()
        team = session.get(TeamModel, id)
        if not team:
            return False
        session.delete(team)
        session.commit()
        return True