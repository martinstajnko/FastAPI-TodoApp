from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


POSTGRESQL_DATABASE_URL = 'postgresql+psycopg2://martin:test123@localhost/todoappdb'
# As a user we need to use superuser

#SQLAlchemy engine
engine = create_engine(POSTGRESQL_DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
