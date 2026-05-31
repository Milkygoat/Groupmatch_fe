from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

connect_args = {}
if "aivencloud" in settings.DATABASE_URL:
    import ssl
    connect_args["ssl"] = {"ssl_cert_reqs": ssl.CERT_NONE} # Enable SSL for Aiven, ignoring cert validation to avoid CA cert issues

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
