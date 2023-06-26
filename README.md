# Project Name: Transaction Tracker

## Project Description

The Transaction Tracker is a web application that allows users to track their financial transactions and gain insights into their spending habits. It provides a user-friendly interface for managing income, expenses, and other financial activities.

## Directory Structure

The project's directory structure is as follows:

```
transaction-tracker/
  ├── app.py              # Backend API (Flask application)
  ├── Dockerfile              # Docker configuration for backend
  ├── client/                 # Frontend client
  │   ├── src/                # Source files
  │   ├── public/             # Public assets
  │   ├── ...
  │   └── Dockerfile          # Docker configuration for frontend
  ├── docker-compose.yml      # Docker Compose configuration
  └── README.md               # Project documentation
```

## Configuration

- Backend Configuration:
  - The backend API is implemented in `backend.py`.
  - No additional configuration is required.

- Frontend Configuration:
  - The frontend client is located in the `client` directory.
  - API endpoint configuration can be updated in the frontend's source files, as needed.

- Docker Configuration:
  - The project uses Docker Compose for containerization.
  - Docker images are built using the respective Dockerfiles for the backend and frontend.
  - The `docker-compose.yml` file defines the services and their configurations.

## Getting Started

To run the Transaction Tracker locally using Docker, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Amool-kk/flask-server.git
   cd flask-server
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This will build the Docker images and start the backend API and frontend client as separate containers.

3. Access the application:

   - Backend API: Open `http://localhost:5000` in your preferred browser.
   - Frontend Client: Open `http://localhost:3000` in your preferred browser.

   The Transaction Tracker application should now be up and running locally on your machine.

## License

This project is licensed under the [MIT License](LICENSE).

Please make sure to update the configuration and directory structure sections to match your project's actual setup and requirements.