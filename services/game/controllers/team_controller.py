from typing import List
from fastapi import HTTPException, status

from services.game.repository.team_repo import TeamRepo
from services.game.models.team_model import TeamUpdate, TeamCreate, TeamRead


def update_team(id: int, team: TeamUpdate) -> TeamRead:
    updated_team = TeamRepo().update_team(id, team)
    if not updated_team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
    return updated_team


def add_team(team: TeamCreate) -> TeamRead:
    return TeamRepo().add_team(team)


def get_team(id: int) -> TeamRead:
    team = TeamRepo().get_team(id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
    return team


def get_all_teams(offset: int, limit: int) -> List[TeamRead]:
    teams = TeamRepo().get_all_teams(offset, limit)
    if not teams:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Team found.")
    return teams


def detete_team(id: int):
    detete_result = TeamRepo().delete_team(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
    return detete_result
