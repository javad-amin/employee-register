# Employee Register

## General Notes
- The intended use of the project is to manage employee information.
- There is a main FastAPI app with a Employee schema.
- A made up MemoryDB database is injected to the main function.
- Currently there are three endpoints for retrieving all employees, adding an employee and removing an employee.
- As FastAPI was used the automated swagger documentation can be found at `/docs` path.

## How to run the project
To run the API with [docker-compose](https://docs.docker.com/engine/reference/commandline/compose_up/) simply use the following command

    docker-compose up -d

If you prefer to run the application locally follow the bellow steps

- Install [poetry](https://python-poetry.org/docs/) 
- Activate your virtual environment `$ poetry shell`
- Install the dependencies  `$ poetry install`
- Set your python path `export PYTHONPATH=src`
- Start the FastAPI server  `uvicorn src.main:app --port 8000 --reload` 

## Endpoints
### List All Employees 
#### Request
* GET /
#### Response
* Response: 200 HttpResponse with all the existing employees.


### Add An Employee
#### Request
* POST /employee
```json
{
    "first_name": "string: Employees first name (Required)",
    "last_name": "string: Employees last name (Optional)",
    "email": "string: Employees email address (Required, must be unique)"
}
```
#### Response
* Response: 200 HttpResponse with the currently added employee
* Response: 400 HttpResponse email already registered


### Remove An Employee
#### Request
* DELETE /employee/\<id\>
#### Response
* Response: 200 HttpResponse successfully removed the employee
* Response: 404 HttpResponse employee with id was not found


## Usage
Now either use a tool like postman to test the endpoints or navigate to `127.0.0.1:8000/docs` in your browser for a Swagger docs.

### Using Curl
* List employees
```bash
curl --location --request GET 'localhost:8000/'
```

* Add employees
```bash
curl --location --request POST 'localhost:8000/employee' \
--header 'Content-Type: application/json' \
--data-raw '{"first_name": "dr", "last_name":"who", "email": "dr@who.com"}'
```

* Remove employees (Replace UUID)
```bash
curl --location --request DELETE 'localhost:8000/employee/<UUID>'
```

## Linting, typing & Tests:
`flake8` and `mypy` are used for linting and type checking.
Use `pytest tests` to run the existing unit tests.


## Next Steps
* Add more endpoints for retrieving a single employee and updating existing employees.
* Add pagination for listing the employees for better performance.
* Use async with a real database.
* Add authentication.
* Add CI and enforce the linting, typing and unittest.
* The unit tests for main could be improved with mocking a database and separating the tests.

