from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 

import uvicorn

# Import the models and database handling module
from models import *
from model import handle_db as db

# Create a FastAPI application instance
app = FastAPI()

# Mount static files for CSS and images
app.mount("/css", StaticFiles(directory="app/templates/css"), name="css")
app.mount("/images", StaticFiles(directory="app/templates/images"), name="images")


# Create a Jinja2 template instance, allows to render HTML templates
templates = Jinja2Templates(directory="app/templates/html")


# Define a route for the root URL ("/") that renders the index page
@app.get("/")
def index(req: Request):
    """"
    Render the index page with a list of scholarships.
    Args:
        req (Request): The request object.
    
    Returns:
        HTML response with the index page.
    """
    DB = db.HandleDB()
    raw_scholarships = DB.get_all()

    print(raw_scholarships)

    # Convertir cada tupla en un diccionario
    scholarships = [
        {"id": s[0], "name": s[1], "description": s[2], "price": s[3], "image": s[4]}
        for s in raw_scholarships
    ]

    return templates.TemplateResponse(
        name="index.html", context={"request": req, "scholarships": scholarships}
        )

#Endpoint for the FastAPI application

if __name__ == "__main__":
    uvicorn.run('main:app')