from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update the PostgreSQL connection details
POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "password"
POSTGRES_DB = "tasks"
POSTGRES_HOST = "localhost"  # Assuming the database is running locally
POSTGRES_PORT = "5432"

# Define the PostgreSQL connection URL
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
