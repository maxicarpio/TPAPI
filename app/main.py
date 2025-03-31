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
def index(req: Request): #req is the request object, in this case is the request of the user
    """"
    Render the index page with a list of scholarships.
    Args:
        req (Request): The request object.
    
    Returns:
        HTML response with the index page.
    """
    DB = db.HandleDB()
    raw_scholarships = DB.get_all() # Get all scholarships from the database

    print(raw_scholarships)

    #Convert the list of tuples into a list of dictionaries
    scholarships = [
        # Convert each tuple into a dictionary with keys
        {"id": scholarship[0], "name": scholarship[1], "description": scholarship[2], "price": scholarship[3], "image": scholarship[4]}
        for scholarship in raw_scholarships
    ] #list = [{item to add} for item in list]

    # Render the index.html template with the list of scholarships
    return templates.TemplateResponse(
        name="index.html", context={"request": req, "scholarships": scholarships} # Pass the scholarships to the template
    )

#Endpoints for the FastAPI application
@app.get("/scholarships/{scholarship_id}")
def scholarship(req: Request, scholarship_id: int):
    """
    Render the scholarship page with details of a specific scholarship.
    Args:
        req (Request): The request object.
        scholarship_id (int): The ID of the scholarship to display.
    
    Returns:
        HTML response with the scholarship page.
    """
    try:
        DB = db.HandleDB()
        raw_scholarship = DB.get_only(scholarship_id)

        if raw_scholarship is None:
            print({"status": "error", "message": "Scholarship not found."})

        #Convert the tuple into a dictionary with keys
        scholarship = {
            "id": raw_scholarship[0],
            "name": raw_scholarship[1],
            "description": raw_scholarship[2],
            "price": raw_scholarship[3],
            "image": raw_scholarship[4]
        }

        return scholarship
    except Exception as e: #Handle any exceptions that occur during the process
        print("Error:", e)
        return {"status": "error", "message": str(e)}

# Endpoint to add a new scholarship
@app.post("/add_scholarship")
def add_scholarship(scholarship: Scholarship):
    """
    Add a new scholarship to the database.
    Args:
        scholarship (Scholarship): The scholarship data to add.
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        scholarship_data = scholarship.model_dump() #Convert the Pydantic model to a dictionary, this new model doesn't have a dict() method. Instead it has a model_dump() method.
        print("Data received: ", scholarship_data)

        DB = db.HandleDB() #Create a database handler instance
        DB.insert(scholarship_data) 

        return {"status": "success", "message": "Scholarship added successfully."}
    except Exception as e: #Handle any exceptions that occur during the process
        print("Error:", e)
        return {"status": "error", "message": str(e)}

# Endpoint to delete a scholarship
@app.delete("/delete_scholarship/{scholarship_id}")
def delete_scholarship(scholarship_id: int):
    """
    Delete a scholarship from the database.
    Args:
        scholarship_id (int): The ID of the scholarship to delete.
    
    Returns:
        JSON response indicating success or failure.
    """
    DB = db.HandleDB()
    DB.delete_only(scholarship_id)

    return {"status": "success", "message": "Scholarship deleted successfully."}

# Endpoint to modify a scholarship
@app.put("/modify_scholarship/{scholarship_id}")
def modify_scholarship(scholarship_id: int, req: Request, scholarship: Scholarship):
    """
    Modify a scholarship in the database.
    Args:
        scholarship_id (int): The ID of the scholarship to modify.
        req (Request): The request object containing the updated scholarship data.
    
    Returns:
        JSON response indicating success or failure.
    """
    DB = db.HandleDB()
    scholarship_data = scholarship.model_dump()
    print("Data received: ", scholarship_data)


    # Update the scholarship data in the database
    DB.modify(scholarship_id, scholarship_data)

    return {"status": "success", "message": "Scholarship modified successfully."}

# Endpoint to delete all scholarships
@app.delete("/delete_all_scholarships")
def delete_all_scholarships():
    """
    Delete all scholarships from the database.
    Args:
        None
    
    Returns:
        JSON response indicating success or failure.
    """
    DB = db.HandleDB()
    DB.delete_all()

    return {"status": "success", "message": "All scholarships deleted successfully."}


# Run the FastAPI application using Uvicorn server
if __name__ == "__main__":
    uvicorn.run('main:app')