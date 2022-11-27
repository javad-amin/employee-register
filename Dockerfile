FROM python:3.10


WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry 
RUN poetry install
COPY . .
ENV PYTHONPATH=src
CMD ["poetry", "run", "python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]