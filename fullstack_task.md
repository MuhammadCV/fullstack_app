# Task Manager Project

## Objective

Build a simple web application with Django that includes a REST API, background task processing using Celery, and a basic front-end component, all orchestrated with Docker Compose.

## Requirements

### Django Project

- Create a Django project and a simple app.
- Set up a basic model (e.g., Task with fields like title, description, completed).

### Django Rest Framework

- Create API endpoints for CRUD operations on the Task model.

### Celery

- Set up Celery to handle background tasks.
- Create a simple task, such as sending an email notification when a new Task is created or updated.

### Django Celery

- Integrate Celery with Django and ensure that tasks are scheduled and executed properly.

### Docker Compose

- Create a Dockerfile for the Django app.
- Create a docker-compose.yml to orchestrate the Django app, a PostgreSQL database, and a Redis instance for Celery.

### Front-End Component

- Create a simple React component to display a list of tasks.
- The choice of fetching and storing the data is left up to you - (e.g., using fetch, Axios) and managing app state (e.g., using React state, Redux).

## Steps

### Set up Django

1. Create a new Django project and app.
2. Define the Task model.
3. Set up Django Rest Framework and create serializers and viewsets for the Task model.
4. Configure URLs and routing.

### Set up Celery

1. Install Celery and configure it in the Django settings.
2. Create a simple Celery task.
3. Set up a Redis broker and backend.

### Dockerize the Application

1. Write a Dockerfile for the Django application.
2. Write a docker-compose.yml file to run the Django app, PostgreSQL, and Redis.
3. Ensure that all services can communicate with each other.

### Front-End Component

1. Set up a basic React application.
2. Create a component to fetch and display a list of tasks from the API.
3. Provide flexibility in choosing the data fetching and state management approach.

### Testing

1. Test the API endpoints using a tool like Postman.
2. Verify that Celery tasks are executed in the background.
3. Ensure the React component displays the data correctly.

### Documentation

Write a brief README with instructions on how to set up and run the project.
