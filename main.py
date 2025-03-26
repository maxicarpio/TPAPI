from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
import uvicorn
from models import *

app = FastAPI()
app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/images", StaticFiles(directory="templates/images"), name="images")

templates = Jinja2Templates(directory="templates/html")

@app.get("/")
def index(req: Request):

    #Create a list of scholarships (provisory)
    scholarships = [
        Scholarship(id=1, image="/images/govuk.jpeg", name="Regional Student Competition", description="Description 1", price=1000),
        Scholarship(id=2, image="/images/govuk.jpeg", name="Scholarship 2", description="Description 2", price=2000),
        Scholarship(id=3, image="/images/govuk.jpeg", name="Scholarship 3", description="Description 3", price=3000)
    ]

    return templates.TemplateResponse(
        name="index.html", context={"request": req, "scholarships": scholarships}
        )

if __name__ == "__main__":
    uvicorn.run('main:app')