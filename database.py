from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
import re


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

SQLALCHEMY_DATABASE_URL = uri
engine =create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
