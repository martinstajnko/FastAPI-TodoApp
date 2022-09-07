# ORIGINAL

####
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# POSTGRESQL_DATABASE_URL = 'postgresql://martin:test123@localhost/todoappdb'
# # As a user we need to use superuser

# #SQLAlchemy engine
# engine = create_engine(POSTGRESQL_DATABASE_URL)

# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
####


# When using with Heroku
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


POSTGRESQL_DATABASE_URL = os.environ.get('DATABASE_URL')
if POSTGRESQL_DATABASE_URL.startswith("postgres://"):
    POSTGRESQL_DATABASE_URL = POSTGRESQL_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# As a user we need to use superuser

#SQLAlchemy engine
engine = create_engine(POSTGRESQL_DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()