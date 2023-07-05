# Timetabling

## Badges

![Unit Tests](https://github.com/jvfd3/UENF-timetabling/actions/workflows/unit_tests.yml/badge.svg)
![Integration Tests](https://github.com/jvfd3/UENF-timetabling/actions/workflows/integration_tests.yml/badge.svg)
![Updating to Cloud](https://github.com/jvfd3/UENF-timetabling/actions/workflows/update_files_on_cloud.yml/badge.svg)

## What is needed?

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
  - from the `timetabling` folder:
    - "uvicorn file_name:server_instance --reload" (Reload only while in develop mode)
    - `uvicorn app:app --reload`
  - Obs.: Has auto docs at `/docs`

## Acknowledgments

The original structure of an web app with fasAPI was inspired by [Patrick Loeber's][LinkYouTube].

[LinkYouTube]: https://youtu.be/3vfum74ggHE
