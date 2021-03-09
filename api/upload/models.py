from sqlalchemy import Column, String, Integer, ForeignKey

from api.database import Base


class File_Upload(Base):

    __tablename__ = "file_upload"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    nom = Column(String, nullable=False)


class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    id_file = Column(Integer, ForeignKey('file_upload.id'), nullable=False)
    uniquId = Column(String, nullable=False)
    information = Column(String, nullable=False)
    valeur = Column(String, nullable=False)
