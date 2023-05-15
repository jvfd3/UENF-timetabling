# UENF-timetabling

![tests](https://github.com/jvfd3/UENF-timetabling/actions/workflows/python_tests.yml/badge.svg)

---

## Setup

To run this project, you will need to create and activate a Python virtual environment and install the dependencies listed in the requirements.txt file. Follow these steps:

### 1. Create and activate the virtual environment

#### 1.1 Open a command prompt and navigate to the project folder. Then run

- Linux / Mac:
  <!-- - `python3 -m venv env` -->
  <!-- - `source env/bin/activate` -->

```bash
    python3 -m venv env
```

```bash
    source env/bin/activate
```

- Windows

```bash
python -m venv env
```

```bash
venv\Scripts\activate.bat
```

This will create a folder called `env` inside the project folder, where the virtual environment files will be stored.
You should see `(env)` at the beginning of your prompt, indicating that the virtual environment is active.

### 1.2 Install the requirements

```bash
    pip install -r requirements.txt
```

This will install all the packages listed in the requirements.txt file in your virtual environment.

You are now ready to run the project!

## Use

- To start the server run:

```bash
uvicorn main:app --reload
```
