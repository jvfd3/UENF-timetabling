""" App """

from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()


# Dependency
def get_db():
    """ GetDB """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    """ Home """
    return "Test"





@app.get("/todo")
def todo_home(request: Request, db: Session = Depends(get_db)):
    """ Todo Home """
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "todo_list": todos})


@app.post("/todo/add")
def todo_add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()

    url = app.url_path_for("todo_home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/todo/update/{todo_id}")
def todo_update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    """ Update """
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = app.url_path_for("todo_home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/todo/delete/{todo_id}")
def todo_delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    """ Delete """
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for("todo_home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
