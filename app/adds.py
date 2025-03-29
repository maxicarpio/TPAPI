from model import handle_db as db

DB = db.HandleDB()

def add_data():
    """
    Function to add data to the database.
    Args:
        None
    Returns:
        None
    """
    decision = True
    while decision != False:
        data = {}

        name = input("Enter the scholarship name: ")
        description = input("Enter the scholarship description: ")
        price = int(input("Enter the scholarship price: "))
        image = input("Enter the scholarship url: ")
        decision = input("Do you want to continue? (y/n) ")
        if decision == "n":
            decision = False
        
        data = {
            "name": name,
            "description": description,
            "price": price,
            "image": image
        }

        DB.insert(data)

add = add_data()