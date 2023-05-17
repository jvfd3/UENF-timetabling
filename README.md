# What is needed?

Disclaimer: All code here was based on the code created by [Patrick Loeber][LinkYouTube].

[LinkYouTube]: https://youtu.be/3vfum74ggHE

- Come to this folder from project root
  - `cd Files/hello_world`
- Create Python's Virtual Environment
  - `python3 -m venv venv`
  - Activate venv
    - Ubuntu
      - `. venv/bin/activate`
    - Windows
      - `. venv\Scripts\activate.bat`
  - `pip install fastapi`
  - ASGI Server
    - `pip install "uvicorn[standard]"`
  - Template and DB support
    - `pip install python-multipart sqlalchemy jinja2`
- Create 4 files
  - templates/base.html
  - app.py
  - database.py
  - models.py
- Start Server
  - "uvicorn file_name:server_instance --reload" (Reload only while in develop mode)
  - `uvicorn app:app --reload`
  - Obs.: Has auto docs at `/docs`
