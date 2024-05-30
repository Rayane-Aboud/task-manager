from fastapi import APIRouter
from .crud import get_projects_service, get_single_project_service
from models import Project
router = APIRouter()
"""
@router.post("/new")
def create_project():
    pass



@router.post("/{user_id}/{project_id}/settings")
def get_settings():
    pass
    
"""

@router.get("/projects",tags=["posts"])
async def get_projects() :
    return get_projects_service()


@router.get("/projects/{project_id}",tags=["posts"])
async def get_single_project(project_id:int):
    return get_single_project_service(id=project_id)

@router.post("/projects",tags=["posts"])
async def create_project(project:Project):