# SQL Playground

A Dockerized PostgreSQL server with a pgAdmin 4 interface for local development, plus Python/psycopg scripts in `pg_utils/` to create, import, and update database tables.

The datasets used int this project can be found [here](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database)

## Prerequisites

- Docker & Docker Compose  
- Python 3.12+ (optional, if you want to run Python scripts)  
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (optional, for managing the Python environment via `pyproject.toml`)

## 1. Clone & configure

```bash
git clone https://github.com/AdelSiddiquei/sql_playground.git
```

Create a `.env` file in the project root with:

```env
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=bike_store

PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
```

These variables power both the `db` and `pgadmin` services in `docker-compose.yml`.
The datasets used in this project can be found [here](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database), however you are free to put whichever datasets you want into your `data/` folder.

## 2. Launch the stack

```bash
docker-compose up -d          #use the detached -d option so that you can still use your terminal after launching.
```

- **Postgres** is on `localhost:5432`  
- **pgAdmin 4** is on [http://localhost:5050](http://localhost:5050)

### pgAdmin setup

1. Open [http://localhost:5050](http://localhost:5050)  
2. Log in with `${PGADMIN_DEFAULT_EMAIL}` / `${PGADMIN_DEFAULT_PASSWORD}`
3. Create a new server:  
   - **Name**: Local Postgres  
   - **Host**: `db`  
   - **Port**: `5432`  
   - **Username**: `${POSTGRES_USER}`  
   - **Password**: `${POSTGRES_PASSWORD}`  

**NOTE** When working from the pgAdmn container the database host will be `db`, however if connecting to the database container externally, i.e. through a python script it will be different.

## 3. Next Steps

At this point you have two options for interacting with the database 

1. You may use the pgadmin interface which is very intuitive and has many guides online. 

**OR*

2. You can use the functions set up in pg_utils to interact with and update the database. The instructions for this are detailed below.

## 4. Python / psycopg scripts

All your table-management logic lives in `pg_utils/`. These modules expose functions to:

- Create tables  
- Import data  
- Update existing records  

### 4.1. Python environment

#### a) Using a plain venv

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

#### b) Using uv

```bash
pip install uv
uv sync  # reads pyproject.toml to set up .venv and uv.lock
source .venv/bin/activate
```

Once the environment is ready, you can write scripts using the functions from `pg_utils/`

### 4.2. Example usage

See loading_script.py for an example of how to use the functions from pg_utils

## Project Layout

```text
.
├── data/              # .csv dataset files
├── docker-compose.yml
├── Dockerfile         # for Python scripts container
├── pgdata/            # Postgres data volume
├── pg_utils/          # helper modules for interacting with database
│   ├── __init__.py
│   └── ...
├── requirements.txt
├── pyproject.toml     # project metadata
├── uv.lock            # locked Python deps for uv
└── README.md          # this file
```

## Tear down

```bash
docker-compose down -v
```
**NOTE**: The -v option deletes any named volumes in the container when closing it. This is necessary to avoid conflicts with our mounted directory `pgdata/` in future sessions. If you ever wish to start fresh when launching, simply rename/delete `pgdata/`, or move it outside of the working directory.

You now have a local Postgres + pgAdmin stack, plus a Python layer to automate table and data chores. Enjoy!

## Future Work
These are ideas for future updates to the package:
- Add to pg_utils so that more querys can be can be done easily.

