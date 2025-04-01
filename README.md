# API Rest for Scholarship Data Center

This API allows you to post, modify, delete and get information from a SQLite database related to scholarships published on a web page.

## Instalation

Check out the requirements in requirements.txt and install all the libraries to execute the program successfully.

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

* Endpoints: 

```/scholarships (GET)```: Gets all scholarships.

```/scholarships/{id} (GET)```: Gets a specific scholarship by ID.

```/scholarships (POST)```: Creates a scholarship.

```/scholarships/{id} (PUT)```: Modifies an existing scholarship.

```/scholarships/{id} (DELETE)```: Deletes a scholarship by ID.
