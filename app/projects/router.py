from fastapi import APIRouter

router = APIRouter(prefix="{user_id}")

@router.post("/new")
def create_project():
    pass



@router.post("{user_id}/{project_id}/settings")
def get_settings():
    pass

