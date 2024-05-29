from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#using sqllite (file called sql_app.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# engine is the database connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#factory for creating new SQLAlchemy sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

# SQLAlchemy's ORM  system uses this base class to define ORM models
Base = declarative_base()
