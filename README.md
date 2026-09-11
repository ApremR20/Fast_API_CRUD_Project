# FastAPI CRUD Operations Backend

## Project Overview

This project is a basic backend application developed using **Python and FastAPI** to understand and implement CRUD (Create, Read, Update, Delete) operations through REST API endpoints.

The project focuses on backend development concepts, API development, request handling, and database connectivity.

## Technologies Used

* Python
* FastAPI
* REST API
* MySQL
* SQLAlchemy
* Uvicorn

## Features

* Create new records
* Retrieve records
* Update existing records
* Delete records
* Handle API requests and responses
* Backend API development using FastAPI
* Database connectivity with MySQL
* Basic database operations using SQLAlchemy

## CRUD Operations

| Operation | HTTP Method | Purpose                   |
| --------- | ----------- | ------------------------- |
| Create    | POST        | Create a new record       |
| Read      | GET         | Retrieve existing records |
| Update    | PUT         | Update an existing record |
| Delete    | DELETE      | Delete a record           |

## Database Connectivity

I also implemented general **MySQL database connectivity** using Python and SQLAlchemy.

The database connection allows the FastAPI backend to communicate with a MySQL database and perform basic database operations.

### Database Components

* MySQL
* SQLAlchemy
* SQLAlchemy ORM
* Database sessions
* CRUD operations

## API Documentation

FastAPI provides interactive API documentation automatically.

After starting the application, the Swagger UI can be accessed at:

```text
http://127.0.0.1:8000/docs
```

ReDoc is also available at:

```text
http://127.0.0.1:8000/redoc
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd fastapi-crud-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create a MySQL database and configure the database connection in the application.

**Important:** Do not upload your actual MySQL password or other credentials to GitHub.

Use environment variables or a `.env` file for sensitive database credentials.

### 7. Start the FastAPI application

If your application entry point is `app/main.py`:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## What I Learned

Through this project, I gained practical experience with:

* FastAPI backend development
* REST API concepts
* CRUD operations
* HTTP methods
* Request and response handling
* MySQL database connectivity
* SQLAlchemy ORM
* Database sessions
* API testing using Swagger UI
* Python backend development

## Future Improvements

* Add authentication and authorization
* Add input validation
* Improve error handling
* Add database migrations
* Add automated API testing
* Deploy the application to a cloud platform

## Author

**Prem Kumar Angirekula**

LinkedIn: https://www.linkedin.com/in/premkumar-angirekula-12ba69311

GitHub: https://github.com/ApremR20
