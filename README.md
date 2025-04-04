# API Rest for Scholarship Data Center

This API allows you to post, modify, delete and get information from a SQLite database related to scholarships published on a web page.

## Instalation

Check out the requirements in requirements.txt and install all the libraries to execute the program successfully  by:

```bash
pip install -r requirements.txt
```

## Structure

* app: Aplication code
    * model: Data modelling and database interactions
    * templates: HTML, CSS and images templates
        * css: Visual styling (fonts, etc.)
        * html: Index page only
        * images: image assets
    * main.py: main application file
    * models.py: Python class to handle data structure
* scholarships.db: SQLite database file

## Database 

The SQLite database `scholarships.db` contains a table named `scholarships` with the following columns:

| Column      | Data Type   | Description                               |
| ----------- | ----------- | ----------------------------------------- |
| id          | INTEGER     | Unique identifier for the scholarship     |
| title       | TEXT        | Title of the scholarship                  |
| description | TEXT        | Detailed description of the scholarship   |
| price       | TEXT        | Scholarship price                         |
| image       | TEXT        | image path                                |

## Usage

* Execute API:

```bash
python main.py
```

Click on the terminal the url.

* Endpoints: 

You have to use SwaggerUI to visualize documentation, add '/docs' at the end of the url that the API provides.

```/scholarships (GET)```: Gets all scholarships.

```/scholarships/{id} (GET)```: Gets a specific scholarship by ID.

```/scholarships (POST)```: Creates a scholarship.

```/scholarships/{id} (PUT)```: Modifies an existing scholarship.

```/scholarships/{id} (DELETE)```: Deletes a scholarship by ID.

To end all process kill the terminal.
