# API Rest for Scholarship Data Center

This API allows you to post, modify, delete and get information from a SQLite database.

## Instalation

Check out the requirements in requirements.txt and intall all the libraries to execute the program succesfully.

```bash
pip install -r requirements.txt
```

## Structure

* app: Global code
* model: Data modelling and database
* templates: html, css and images templates
* scholarships.db: SQLite database

## Usage

* Execute API:
```bash
python main.py
```

*Endpoints: 
```/scholarships (GET)```:Obtiene todas las becas.
```/scholarships/{id} (GET)```: Obtiene una beca por su ID.
```/scholarships (POST)```: Crea una nueva beca.
```/scholarships/{id} (PUT)```: Actualiza una beca existente.
```/scholarships/{id} (DELETE)```: Elimina una beca.