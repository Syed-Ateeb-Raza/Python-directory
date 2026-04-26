from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string — update with your password!
DATABASE_URL = "postgresql://postgres:admin@localhost/fastapi_db"

# Create the engine — this is the connection to PostgreSQL
engine = create_engine(DATABASE_URL)

# Each request gets its own database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our database models
Base = declarative_base()


# Dependency — gives each route its own db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()