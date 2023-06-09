""" App """

from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.staticfiles import StaticFiles  # Just to add Favicon

from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="./templates")

app = FastAPI()

app.mount(
    "/static", StaticFiles(directory="static"), name="static"
)  # Just to add Favicon
# Note: if you deal with favicon in chrome,
# remember to do shift+f5 to reload without cached data

# Dependency
def get_db():
    """ GetDB """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/table")
def time_slots_table(request: Request, db: Session = Depends(get_db)):
    """ table """
    time_slots = db.query(models.TimeSlot).all()
    classes = map_timeslots_to_classes(time_slots)

    print(models.TimeSlot.slot.type)  # Integer
    return templates.TemplateResponse(
        "tt_table.html", {"request": request, "time_slot_list": time_slots, "classes": classes}
    )


@app.post("/table/add")
def time_slot_add_table(
    request: Request,
    turma_id: str = Form(...),
    time_slot: str = Form(),
    db: Session = Depends(get_db),
):
    """ Add Time Slots"""
    new_time_slot = models.TimeSlot(turma_id=turma_id, slot=int(time_slot))
    db.add(new_time_slot)
    db.commit()

    url = app.url_path_for("time_slots_table")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    """ Home """
    time_slots = db.query(models.TimeSlot).all()
    return templates.TemplateResponse(
        "tt_index.html", {"request": request, "time_slot_list": time_slots}
    )


@app.post("/add")
def time_slot_add(
    request: Request,
    turma_id: str = Form(...),
    time_slot: str = Form(),
    db: Session = Depends(get_db),
):
    """ Add Time Slots"""
    new_time_slot = models.TimeSlot(turma_id=turma_id, slot=int(time_slot))
    db.add(new_time_slot)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{time_slot_id}")
def time_slot_delete(
    request: Request, time_slot_id: int, db: Session = Depends(get_db)
):
    """ Delete """
    time_slot = db.query(models.TimeSlot).filter(models.TimeSlot.id == time_slot_id).first()
    db.delete(time_slot)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.get("/update/{time_slot_id}")
def time_slot_update(request: Request,
                     time_slot_id: int, 
                     turma_id: str = Form(...),
                     time_slot: str = Form(),
                     db: Session = Depends(get_db)
):
    """ Update """
    time_slot = db.query(models.TimeSlot).filter(models.TimeSlot.id == time_slot_id).first()
    time_slot.turma_id = turma_id
    time_slot.slot = time_slot
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)



@app.get("/todo")
def todo_home(request: Request, db: Session = Depends(get_db)):
    """ Todo Home """
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse(
        "base.html", {"request": request, "todo_list": todos}
    )


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


def map_timeslots_to_classes(time_slots):
    classes = {
        "08:00-10:00": {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "10:00-12:00": {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "14:00-16:00": {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": []
        },
        "16:00-18:00": {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": []
        }}

    rows = ["08:00-10:00", "10:00-12:00", "14:00-16:00", "16:00-18:00"]
    columns = ["mon", "tue", "wed", "thu", "fri"]

    for time_slot in time_slots:
        class_slot = int(time_slot.slot) 
        if class_slot < 19 and class_slot >= 0:    
            
            row = rows[class_slot // 5]
            column = columns[class_slot % 5] 

            classes[row][column].append(time_slot) 
    return classes