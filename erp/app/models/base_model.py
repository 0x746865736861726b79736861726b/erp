from uuid import uuid4

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: uuid4
    __name__: str

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
