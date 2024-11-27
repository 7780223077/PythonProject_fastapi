from app.database import Base
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime

class Post(Base):
    __tablename__ = 'post'

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title:Mapped[str] = mapped_column(String, nullable=False, index=True)
    content:Mapped[str] = mapped_column(String, nullable=False, index=True)
    published:Mapped[bool] = mapped_column(Boolean, server_default='TRUE', nullable=False)
    created_at:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    
