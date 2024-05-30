
projects = [
    {
        "id":1,
        "title":"first flow",
        "description":"this is the first project",
        "owner_id":1,
        "tasks":[]
    },
    {
        "id":2,
        "title":"first flow",
        "description":"this is the first project",
        "owner_id":1,
        "tasks":[]
    }
]



def get_projects_service():
    return {"projects":projects}

def get_single_project_service(id:int):
    #change the logic when integrating a db
        
    for project in projects:
        if project["id"] == id:
            return {
                "data": project
            }
    return {
            "error": "No such post with the supplied ID."
        }

