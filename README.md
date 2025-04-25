
# FastAPI + Supabase Authentication with Docker

This project demonstrates how to set up a FastAPI application that integrates with [Supabase](https://supabase.io) for user authentication. The app is containerized using Docker and Docker Compose for easy deployment and management.

## Features
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **Supabase**: An open-source Firebase alternative that provides authentication, databases, and storage.
- **Docker & Docker Compose**: Containerization for easy deployment.

## Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── auth.py              # Authentication logic
│   ├── models.py            # Database models (optional)
│   └── ...
├── .env                     # Environment variables
├── Dockerfile               # Dockerfile for building the app container
├── docker-compose.yml       # Docker Compose file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Prerequisites
Before running this application, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-supabase-docker.git
   cd fastapi-supabase-docker
   ```

2. Create a `.env` file in the root directory of the project with the following content:

   ```env
   # Supabase Environment Variables
   SUPABASE_URL=https://your-supabase-project-url.supabase.co
   SUPABASE_ANON_KEY=your-anon-key
   SUPABASE_SERVICE_KEY=your-service-role-key

   # FastAPI Configuration
   SECRET_KEY=your-jwt-secret-key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   EXPECTED_AUDIENCE=authenticated
   ```

   Replace `your-supabase-project-url`, `your-anon-key`, `your-service-role-key`, and `your-jwt-secret-key` with your actual Supabase credentials and JWT secret key.

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Docker Setup

### Build the Docker image

To build the Docker image, run the following command:

```bash
docker-compose build
```

### Start the application with Docker Compose

Once the Docker image is built, start the FastAPI application and the necessary services using Docker Compose:

```bash
docker-compose up -d
```

This will start the FastAPI application in the background. By default, the application will be accessible at `http://localhost:8000`.

### Access Logs

To view the logs of your running container:

```bash
docker-compose logs -f
```

## Environment Variables

Below is a list of environment variables that should be configured in the `.env` file:

- `SUPABASE_URL`: The URL of your Supabase project (find it in the Supabase dashboard).
- `SUPABASE_ANON_KEY`: The anonymous key for accessing the Supabase API (find it in the Supabase dashboard).
- `SUPABASE_SERVICE_KEY`: The service key for accessing Supabase with higher privileges (find it in the Supabase dashboard).
- `SECRET_KEY`: The secret key for signing JWT tokens. You can generate one using `openssl rand -hex 32`.
- `ALGORITHM`: The algorithm used to encode the JWT token. For example, `HS256`.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: The expiration time for the access token in minutes (e.g., `30` minutes).
- `EXPECTED_AUDIENCE`: The expected audience in the token. This should match the value in your Supabase settings (e.g., `authenticated`).

## Running the Application

Once everything is set up, you can interact with the FastAPI app via the following endpoints:

- **Login**: `POST /token` - Request a JWT token by providing a username and password.
- **Protected Route**: `GET /random-test` - A rate-limited route that requires a valid JWT token in the header.

### Example Requests

**Login Request** (to `/token`):
```bash
curl -X 'POST'   'http://localhost:8000/token'   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'username=testuser&password=secretpassword'
```

**Access Protected Route** (to `/random-test`):
```bash
curl -X 'GET'   'http://localhost:8000/random-test'   -H 'Authorization: Bearer <your-jwt-token>'
```

## Stopping the Application

To stop the application and remove the containers, run:

```bash
docker-compose down
```

## Troubleshooting

- **JWT Error**: If you're getting an "Invalid token" error, ensure your JWT token is correctly passed in the `Authorization` header.
- **Missing Environment Variables**: Make sure you have set up the `.env` file correctly with the necessary keys and values.

## Conclusion

This setup allows you to deploy a FastAPI application that integrates seamlessly with Supabase for authentication and is fully containerized using Docker and Docker Compose.

Feel free to extend this project by adding more routes or integrating other Supabase features like the database or file storage.

---

> **Note**: Remember to replace all the example values in the `.env` file with your actual credentials from Supabase.
