## Project & Task Management System – Simple Explanation

### 1. Purpose

This web application lets a user:

- Sign up and log in.
- Reset their password.
- Create projects.
- Add tasks inside projects.
- Mark tasks as done or delete them.

It is a small example of how to build a full web app with FastAPI and a database.

### 2. Technologies

- **FastAPI** – web framework for building APIs and pages.
- **SQLAlchemy** – talks to the database using Python classes instead of raw SQL.
- **SQLite** (via `DATABASE_URL` in `.env`) – development database (can be replaced by PostgreSQL).
- **Jinja2** – HTML templates for pages (login, signup, dashboard).
- **Passlib (pbkdf2_sha256)** – secure password hashing.
- **python-jose** – JWT tokens for the JSON API.
- **Uvicorn** – ASGI server that runs the FastAPI app.

### 3. Structure (Important Files)

- `app/main.py`  
  Creates the FastAPI app, sets up session middleware, static files, and includes routers (`auth_routes`, `dashboard`, `api`). Calls `Base.metadata.create_all(engine)` to create tables.

- `app/database.py`  
  Reads `DATABASE_URL` from `.env`, creates the SQLAlchemy `engine` and `SessionLocal`, defines `Base` and `get_db()` dependency for DB sessions.

- `app/models.py`  
  Defines 3 tables:
  - `User`: `id`, `email`, `full_name`, `hashed_password`, `created_at`.
  - `Project`: `id`, `name`, `description`, `owner_id`, `created_at`.
  - `Task`: `id`, `title`, `description`, `is_completed`, `project_id`, `created_at`.
  And relationships: a user has many projects; a project has many tasks.

- `app/auth.py`  
  - Hashes and verifies passwords using `pbkdf2_sha256`.
  - Loads `SECRET_KEY` from `.env`.
  - Creates JWT tokens for the API.
  - Provides helper functions to get the current user from the session (HTML) or from a JWT (API).

- `app/schemas.py`  
  Pydantic models for the JSON API:
  - User: `UserCreate`, `UserOut`, `Token`.
  - Project: `ProjectCreate`, `ProjectUpdate`, `ProjectOut`.
  - Task: `TaskCreate`, `TaskUpdate`, `TaskOut`.

- `app/routers/auth_routes.py`  
  HTML-based authentication:
  - `/login` (GET/POST) – login form and handling.
  - `/signup` (GET/POST) – signup form and create user.
  - `/forgot-password` (GET/POST) – reset password.
  - `/logout` – clear session.

- `app/routers/dashboard.py`  
  HTML dashboard and task management:
  - `/dashboard` – shows user projects and their tasks.
  - `POST /projects` – create project.
  - `POST /projects/{project_id}/tasks` – create task.
  - `POST /tasks/{task_id}/toggle` – toggle complete.
  - `POST /tasks/{task_id}/delete` – delete task.

- `app/routers/api.py`  
  JSON REST API for the same data:
  - `/api/signup` and `/api/login` – signup and login with JWT.
  - `/api/me` – current user.
  - `/api/projects` (GET/POST) – list/create projects.
  - `/api/projects/{id}` (GET/PUT/DELETE) – get/update/delete project.
  - `/api/projects/{id}/tasks` (GET/POST) – list/create tasks for a project.
  - `/api/tasks/{id}` (PUT/DELETE) – update/delete a single task.

- `app/templates/*.html`  
  - `base.html` – base layout with navigation and CSS.
  - `login.html` – login page.
  - `signup.html` – signup page.
  - `forgot_password.html` – reset password page.
  - `dashboard.html` – dashboard with projects and tasks.

- `app/static/style.css`  
  Styling for all pages (dark theme, cards, buttons, layout).

- `tests/test_api.py`  
  Tests the API endpoints using `TestClient` and a temporary SQLite database.

- `.env`  
  Holds settings like:
  - `DATABASE_URL=sqlite:///./dev.db`
  - `SECRET_KEY=<random_secret_string>`

### 4. How the HTML Flow Works

1. User visits `/signup` and creates an account. The password is hashed and saved; the user is logged in and redirected to `/dashboard`.
2. On `/login`, the user enters email and password; if correct, `user_id` is stored in the session and the user goes to `/dashboard`.
3. On `/dashboard`, the app loads all projects and tasks for the logged-in user. The user can create projects, add tasks, toggle them done, and delete them.
4. On `/forgot-password`, the user can enter their email and a new password; if the email exists, the password is updated.

### 5. How to Run

1. Install dependencies:

```bash
cd /Users/Ginkgo/Documents/personal/fastapi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create `.env`:

```env
DATABASE_URL=sqlite:///./dev.db
SECRET_KEY=<your_random_secret_string>
```

3. Start the server:

```bash
uvicorn app.main:app --reload --port 8001
```

4. Open in browser:
   - `http://127.0.0.1:8001/signup`
   - `http://127.0.0.1:8001/login`
   - `http://127.0.0.1:8001/dashboard`

