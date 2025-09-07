from sqlmodel import SQLModel,Field,Column
import uuid
from datetime import datetime
from sqlalchemy.dialects import mysql

class Book(SQLModel,table=True):
    __tablename__="books"
    id: uuid.UUID =Field(
        sa_column=Column(
            mysql.CHAR(36),
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    title:str=Field(nullable=False)
    author: str
    publisher: str
    published_date:str
    page_count:int
    language:str
    created_at:datetime=Field(
        sa_column=Column(
            mysql.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at:datetime=Field(
        sa_column=Column(
            mysql.TIMESTAMP,
            default=datetime.now
        )
    )
