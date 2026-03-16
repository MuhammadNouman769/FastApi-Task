## Project & Task Management System (FastAPI)

This is a simple Project & Task Management System built with **FastAPI** and **PostgreSQL**.  
It supports:

- **User signup** (create account)
- **Login / Logout**
- **Password reset** (via "Forgot Password" form)
- **Dashboard** to manage:
  - Projects (create, list)
  - Tasks inside projects (create, update status, delete)

### Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Templates**: Jinja2 (server‑side rendered HTML)

### Project Structure

- `main.py` – FastAPI app entrypoint, route mounting
- `database.py` – DB connection and session management
- `models.py` – SQLAlchemy models (`User`, `Project`, `Task`)
- `auth.py` – Authentication helpers (password hashing, login helpers)
- `routers/` – Route modules:
  - `auth_routes.py` – signup, login, logout, password reset
  - `dashboard.py` – dashboard, project & task management
- `templates/` – HTML pages (login, signup, forgot password, dashboard, etc.)
- `static/` – CSS styles

### Prerequisites

- Python 3.10+
- PostgreSQL running locally (or accessible connection string)

Create a database, for example:

```sql
CREATE DATABASE project_manager;
```

### Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://USER:PASSWORD@localhost:5432/project_manager
SECRET_KEY=replace_with_a_long_random_string
```

Replace `USER` and `PASSWORD` with your PostgreSQL credentials.

### Install & Run

```bash
cd /Users/Ginkgo/Documents/personal/fastapi
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/login` in your browser.

### First-Time Use

1. Go to `/signup` to create a user account.
2. Log in at `/login`.
3. After login you’ll be redirected to `/dashboard`, where you can:
   - Create projects
   - Add tasks to projects
   - Update or delete tasks

### Notes

- This is a simple educational example and omits production features like email verification, real password-reset emails, and role-based authorization.
- Passwords are stored hashed using `passlib`.

