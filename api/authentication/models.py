from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from api.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    identifiant = Column(String, nullable=False)
    password = Column(String, nullable=False)
