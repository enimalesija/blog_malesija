
# A.Malesija Django Blog

## Table of Contents
- [Project Setup](#project-setup)
- [How to Run the Project](#how-to-run-the-project)
- [API Usage](#api-usage)
- [Example Requests](#example-requests)
- [Design Decisions](#design-decisions)
- [Contributing](#contributing)
- [License](#license)

## Project Setup

To set up the project, follow these steps:

### Prerequisites
Ensure you have the following software installed:
- Docker and Docker Compose
- Python 3.9+ (if not using Docker)
- Git (for version control)

### Clone the repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/enimalesija/blog_malesija
cd blog_malesija
```

### Docker Setup (Preferred Method)

1. **Build and Start the Containers**
   
   From the project root directory, run:

   ```bash
   docker-compose build
   docker-compose up
   ```

   This will build the Docker containers and start the application along with a database, using Docker Compose. It may take a while, depending on your machine.

2. **Create the Database and Run Migrations**

   If the application is running for the first time, or if you need to apply migrations, run the following:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create a Superuser (Optional)**

   To access the Django admin panel, create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Manual Setup (Without Docker)

If you prefer not to use Docker, follow these steps:

1. **Install Dependencies**

   Create a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run Migrations**

   Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

3. **Create a Superuser (Optional)**

   Create a superuser if you want to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

4. **Run the Development Server**

   Start the development server:

   ```bash
   python manage.py runserver
   ```

   You can now access the project at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Usage

### Base URL
Once the project is running, the base URL for the API is:

```
http://127.0.0.1:8000/api/posts/
```

You can interact with the various API endpoints that you define in your project.

### Authentication
You may need to authenticate using a **token** or **username/password**. 

- To get a token (if using token-based authentication), you can use the **obtain token endpoint**:

  ```bash
  POST /api/token/
  ```

  Example Request:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/token/ -d '{"username": "admin", "password": "yourpassword"}' -H 'Content-Type: application/json'
  ```

  Example Response:
  ```json
  {
    "access": "your_access_token",
    "refresh": "your_refresh_token"
  }
  ```

- Use the **access token** to authenticate subsequent requests by including it in the Authorization header.

### Example Endpoints

#### 1. **List of Items**

To retrieve a list of items from the database, use the following endpoint:

```bash
GET /api/items/
```

Example Request:
```bash
curl -X GET http://127.0.0.1:8000/api/items/ -H 'Authorization: Bearer your_access_token'
```

Example Response:
```json
[
  {
    "id": 1,
    "name": "Item 1",
    "description": "Description for Item 1"
  },
  {
    "id": 2,
    "name": "Item 2",
    "description": "Description for Item 2"
  }
]
```

#### 2. **Create a New Item**

To create a new item, send a `POST` request to the `/api/items/` endpoint.

```bash
POST /api/items/
```

Example Request:
```bash
curl -X POST http://127.0.0.1:8000/api/items/ -H 'Authorization: Bearer your_access_token' -d '{"name": "New Item", "description": "Description of the new item"}' -H 'Content-Type: application/json'
```

Example Response:
```json
{
  "id": 3,
  "name": "New Item",
  "description": "Description of the new item"
}
```

## Design Decisions

Here are some key design decisions made in this project:

1. **Database Choice: SQLite**  
   For simplicity and ease of setup, I used SQLite as the database for development purposes. SQLite is lightweight and easy to configure, but it can be easily replaced by other databases (e.g., PostgreSQL, MySQL) when transitioning to production. I think SQLite is easier also in localhost environments.

2. **Django Framework**  
   Django was chosen due to the assignment requirements and its robust features for rapid development, including built-in authentication, admin panel, and the ORM for interacting with the database. It also integrates perfectly with Docker for containerization.

3. **Docker for Containerization**  
   Docker was chosen as extra from the requirements to ensure that the development environment is runnable for all machines. This allows for easy onboarding of new developers and a easy setup that avoids environment issues.

4. **Use of Django Migrations**  
   Django migrations are used to track and apply changes to the database schema. This allows us to easily manage database changes, apply them to different environments, and to make sure the consistency in the database schema.

5. **API-First Approach**  
   The project follows an API-first approach, meaning that the primary way to interact with the application is through REST API endpoints (based on the requirements). Django's `Django REST Framework (DRF)` is used for building the APIs, as it provides a comprehensive toolkit for developing RESTful APIs with ease.

6. **Security Considerations**  
   Sensitive data such as passwords are stored securely, and proper authentication mechanisms (e.g., token-based authentication) are in place for API access. Always ensure that sensitive information is protected.

7. **Version Control**  
   The `.gitignore` file includes `db.sqlite3` and other unnecessary files like `*.pyc` to keep the repository clean. This ensures that only source code, migrations, and configuration files are tracked.

## Contributing

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository, make changes, and submit a pull request.

To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Submit a pull request


## License

This project is licensed under the BSD License - see the [LICENSE](LICENSE) file for details.
