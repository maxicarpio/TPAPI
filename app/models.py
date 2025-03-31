from pydantic import BaseModel

#This BaseModel is used to define the structure of the data that will be used in the application.
class Scholarship(BaseModel):
    """
    Scholarship model representing the structure of scholarship data.
    Attributes:
        name (str): Name of the scholarship.
        description (str): Description of the scholarship.
        price (str): Price of the scholarship. This is string to allow for currency symbols or other formatting as 'free'.
        image (str): URL or path to the image associated with the scholarship. You have to use images/example.png due to the way index.html is written.
    """
    name: str
    description: str
    price: str
    image: str
