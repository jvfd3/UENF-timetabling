# What is needed?

Disclaimer: All code here was based on the code created by [Patrick Loeber][LinkYouTube].

[LinkYouTube]: https://youtu.be/3vfum74ggHE

- Create Python's Virtual Environment
  - `python3 -m venv venv`
  - Activate venv
    - Ubuntu
      - `. venv/bin/activate`
    - Windows
      - `. venv\Scripts\activate.bat`
  - `pip install fastapi "uvicorn[standard]" python-multipart sqlalchemy jinja2`
  - ASGI Server: "uvicorn[standard]"
  - Template and DB support
    - python-multipart
    - sqlalchemy
    - jinja2
- Start Server
  - "uvicorn file_name:server_instance --reload" (Reload only while in develop mode)
  - `uvicorn app:app --reload`
  - Obs.: Has auto docs at `/docs`
