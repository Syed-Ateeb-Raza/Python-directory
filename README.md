# My FastAPI Learning Project

so i'm learning FastAPI and this is my practice project. building a REST API with PostgreSQL to understand how all the pieces fit together. will keep updating this as i learn more stuff.

---

## what i've built so far

- connected FastAPI to a PostgreSQL database using SQLAlchemy
- created a User model (basically a table in the DB)
- full CRUD for users (create, read, update, delete)
- passwords are hashed using bcrypt (learned you should NEVER store plain text passwords)
- a basic products router to practice query parameters
- split routes into separate files using APIRouter (much cleaner than dumping everything in main.py)

---

## project files and what they do

```
├── main.py        → the starting point, registers all the routers
├── database.py    → sets up the connection to PostgreSQL
├── models.py      → defines the actual DB tables using SQLAlchemy
├── schemas.py     → Pydantic models for validating data coming in and going out
├── oauth2.py      → going to add JWT auth here (not done yet)
└── routers/
    ├── users.py   → all user routes (signup, login, get, update, delete)
    └── products.py → practicing query params here, no DB yet
```

---

## how to run this locally

**step 1 - create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**step 2 - install the packages**

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] pydantic[email]
```

**step 3 - create the database in PostgreSQL**

```sql
CREATE DATABASE fastapi_db;
```

**step 4 - update the db url in database.py**

```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost/fastapi_db"
```

just replace YOUR_PASSWORD with your actual postgres password

**step 5 - start the server**

```bash
uvicorn main:app --reload
```

the `--reload` flag is super useful, it restarts the server automatically every time you save a file

---

## testing the API

FastAPI auto-generates interactive docs which is honestly one of the coolest things about it

- Swagger UI → http://127.0.0.1:8000/docs (i use this one, you can test everything from the browser)
- ReDoc → http://127.0.0.1:8000/redoc

---

## endpoints

### users

| method | endpoint | what it does |
|---|---|---|
| POST | `/users/` | create a new user |
| GET | `/users/` | get all users |
| GET | `/users/{id}` | get one user by id |
| PUT | `/users/{id}` | update a user |
| DELETE | `/users/{id}` | delete a user |
| POST | `/users/login` | login with email + password |

### products (still basic, no db connected)

| method | endpoint | what it does |
|---|---|---|
| GET | `/products/?category=electronics` | get products, can also pass `limit` and `search` |
| POST | `/products/` | create a product |

---

## things i learned while building this

**why are there two different User schemas?**

`UserCreate` has the password field (for when someone signs up), but `UserResponse` doesn't (you never want to send the password back). took me a bit to understand why you need separate schemas but it makes sense now.

**what is `Depends(get_db)` doing?**

this is dependency injection in FastAPI. instead of manually opening and closing a db session in every route, you just write `db: Session = Depends(get_db)` and FastAPI handles it automatically. pretty neat.

**what does `response_model` do?**

it controls what gets sent back in the response. even if the db object has a password field, FastAPI will strip it out if it's not in the response_model schema. this is how the password never leaks out.

**how does APIRouter work?**

instead of writing all routes in main.py, you create separate router files. each router has a prefix like `/users` so you don't have to repeat it on every route. then in main.py you just do `app.include_router(users.router)` to plug it in.

**password hashing**

using passlib with bcrypt. when a user signs up the password gets hashed before saving to db. on login, `verify_password()` checks if the plain text matches the hash. never storing raw passwords.

---

## stuff i still need to do

- [ ] finish the JWT auth in oauth2.py
- [ ] protect routes so only logged in users can access them
- [ ] add a Product model and connect it to the database
- [ ] maybe add a relationship between users and products

---

## resources i've been using

- https://fastapi.tiangolo.com/ (the official docs are actually really good)
- https://docs.sqlalchemy.org/
- https://docs.pydantic.dev/
