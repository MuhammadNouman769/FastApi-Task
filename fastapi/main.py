from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Task(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None

tasks = [
    {
        "id": 1,
        "title": "Task 1"
    },
    {
        "id": 2,
        "title": "Task 2"
    },
    {
        "id": 3,
        "title": "Task 3"
    }
]


@app.get("/tasks")
def get_task_list():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return {"message": "Task not found"}

@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title
    }
    tasks.append(new_task)
    return new_task


@app.patch("/tasks/{id}")
def update_task(id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == id:
            if task_update.title is not None:
                task["title"] = task_update.title
            return task
    return {"message": "Task not found"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"message": "Task not found"}