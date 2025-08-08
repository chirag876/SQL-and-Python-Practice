from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
# Dependency injection for db session
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        