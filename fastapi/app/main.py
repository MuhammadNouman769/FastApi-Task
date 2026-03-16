from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import os

from dotenv import load_dotenv

from .database import Base, engine
from .routers import auth_routes, dashboard, api

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

secret_key = os.getenv("SECRET_KEY", "change_me_in_env")
app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def root(request: Request):
    if request.session.get("user_id"):
        return RedirectResponse(url="/dashboard")
    return RedirectResponse(url="/login")


app.include_router(auth_routes.router)
app.include_router(dashboard.router)
app.include_router(api.router)

