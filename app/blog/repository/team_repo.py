from app.blog.models.team_model import TeamModel, TeamCreate, TeamRead, TeamUpdate
from app.core.repo import Repo
from sqlmodel import select


class TeamRepo(Repo):
    def add_team(self, team: TeamCreate) -> TeamModel:
        db_team = TeamModel.from_orm(team)
        self.session.add(db_team)
        self.session.commit()
        self.session.refresh(db_team)
        return db_team


    def get_all_teams(self, offset: int, limit: int) -> list[TeamRead]:
        statement = select(TeamModel).offset(offset).limit(limit)
        teams = self.session.exec(statement).all()
        return teams


    def get_team(self, id: int) -> TeamRead:
        return self.session.get(TeamModel, id)

    
    def update_team(self, id: int, team: TeamUpdate) -> TeamRead:
        db_team = self.session.get(TeamModel, id)
        if not db_team:
            return None
        
        team_data = team.dict(exclude_unset=True)
        for key, value in team_data.items():
            setattr(db_team, key, value)
        
        self.session.add(db_team)
        self.session.commit()
        self.session.refresh(db_team)
        return db_team


    def delete_team(self, id: int) -> bool:
        team = self.session.get(TeamModel, id)
        if not team:
            return False
        self.session.delete(team)
        self.session.commit()
        return True