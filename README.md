fastapi-task/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       └── tasks.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── venv/


# FastAPI Task Manager API

A simple Task Manager API built using FastAPI.
This project demonstrates how to build REST APIs with database integration.

## Features

* Create tasks
* Delete tasks
* Get list of tasks
* REST API endpoints
* Database integration

## Tech Stack

* Python
* FastAPI
* SQLite / PostgreSQL
* Git & GitHub

## Installation

Clone the repository

git clone https://github.com/MuhammadNouman769/FastApi-Task.git

Go to project folder

cd FastApi-Task

Create virtual environment

python -m venv venv

Activate environment

Linux / Mac

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

## Run the Project

uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates docs:

Swagger UI
http://127.0.0.1:8000/docs

ReDoc
http://127.0.0.1:8000/redoc

## API Endpoints

GET /tasks → Get all tasks
POST /tasks → Create new task
DELETE /tasks/{id} → Delete task

## Author

Muhammad Nouman

## License

This project is open source and available under the MIT License.
