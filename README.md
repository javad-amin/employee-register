This is a simple API with some CRUD operations build with FastAPI framework.

To run the API in docker simply use the following command

    docker-compose up -d

If you prefer to run the application locally follow the bellow steps

- the first step is to install [poetry](https://python-poetry.org/docs/) 
- Activate a virtual environment `$ poetry shell`
- Install the dependencies  `$ poetry install`
- Set your python path `export PYTHONPATH=src`
- Start the FastAPI server  `uvicorn src.main:app --port 8000 --reload` 

Now either use a tool like postman to test the endpoints or navigate to [127.0.0.1:8000/docs](127.0.0.1:8000/docs) in your browser for a Swagger docs.

Endpoints
- List all existing employees (GET /) 
- Add new Employee (Post /employee)
- Remove Employee by id (DELETE /employee)

Formatting & Tests:
`flake8` and `mypy` are used for format and type checking.
Use `pytest tests` to run the existing unit tests.

