# Task List Application

This project is a task list application built with Django for the backend and React for the frontend. It utilizes Celery for background processing and PostgreSQL for database management.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setting Up the Backend](#setting-up-the-backend)
- [Setting Up the Frontend](#setting-up-the-frontend)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Contributing](#contributing)

## Features

- Create, read, update, and delete tasks.
- Background task processing with Celery for sending notifications.
- User-friendly interface built with React.
- RESTful API using Django Rest Framework.

## Technologies Used

- **Django**: Web framework for the backend.
- **Django Rest Framework**: Toolkit for building Web APIs.
- **PostgreSQL**: Database management system.
- **Celery**: Distributed task queue for handling background tasks.
- **Redis**: In-memory data structure store, used as a message broker for Celery.
- **React**: JavaScript library for building user interfaces.
- **Axios**: Promise-based HTTP client for making API requests.

## Installation

### Clone the Repository

1. **Clone the GitHub Repository**:
   Open your terminal and run:
   ```bash
   git clone https://github.com/MuhammadCV/fullstack_app.git
   cd task-list-app

### Backend (Django)

1. **Create and Activate Conda Environment**: Open your terminal and run:

   ```bash
   conda create --name task python=3.9
   conda activate task`

2. **Install Required Libraries**: Install the necessary Python packages:

   ```bash
   pip install Django
   pip install djangorestframework
   pip install django-cors-headers
   pip install psycopg2-binary
   pip install celery`

### Frontend (React)

1. **Install Node.js**: Download and install Node.js from [nodejs.org](https://nodejs.org/). This will also install npm (Node Package Manager).

2. **Create a React Application**: Use Create React App to set up a new project:

   ```bash
   npx create-react-app task-list-app
   cd task-list-app`

3. **Install Axios**: To handle HTTP requests, install Axios:

   ```bash
    npm install axios`

Setting Up the Project
----------------------

### Setting Up the Backend

1. **Navigate to Your Django Project Directory**: If you have created a Django project named `myproject`, navigate to that directory:

   ```bash
    cd myproject  # or wherever your Django project is located`

3.  **Configure Django Settings**:

   -   Update `settings.py` to include `corsheaders` in `INSTALLED_APPS` and middleware settings.
   -   Set up the database settings for PostgreSQL.
4. **Run Migrations**: Apply migrations to set up your database schema:

   ```bash
   python manage.py migrate`

### Setting Up the Frontend

1. **Navigate to the React App Directory**: If your React app is in the `task-list-app` folder, change to that directory:

   ```bash
   cd task-list-app`

Running the Application
-----------------------

### Start the Django Backend

1. **Start the Django Development Server**: In your Django project directory, run:

   ```bash
   python manage.py runserver`

### Start the Celery Worker

1. **In a New Terminal Window**: Activate your conda environment again and start the Celery worker:

   ```bash
   conda activate task
   celery -A tasks.tasks worker --loglevel=info`

### Start the React Frontend

1. **In Another Terminal Window**: Navigate to your React app directory and start the development server:

   ```bash
   cd task-list-app
   npm start`

API Endpoints
-------------

-   **GET /api/tasks/**: Retrieve the list of tasks.
-   **POST /api/tasks/**: Create a new task.
-   **PUT /api/tasks/{id}/**: Update an existing task.
-   **DELETE /api/tasks/{id}/**: Delete a task.
